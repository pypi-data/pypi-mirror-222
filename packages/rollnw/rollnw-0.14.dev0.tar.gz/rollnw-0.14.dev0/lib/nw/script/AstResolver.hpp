#pragma once

#include "../log.hpp"
#include "../util/string.hpp"
#include "../util/templates.hpp"
#include "Context.hpp"
#include "Nss.hpp"

#include <unordered_map>
#include <vector>

namespace nw::script {

struct ScopeDecl {
    bool ready = false;
    Declaration* decl = nullptr;
};

struct AstResolver : BaseVisitor {
    AstResolver(Nss* parent, std::shared_ptr<Context> ctx)
        : parent_{parent}
        , ctx_{ctx}
    {
    }

    virtual ~AstResolver() = default;

    using ScopeMap = std::unordered_map<std::string, ScopeDecl>;
    using ScopeStack = std::vector<ScopeMap>;

    Nss* parent_ = nullptr;
    std::shared_ptr<Context> ctx_;
    ScopeStack scope_stack_;
    int loop_stack_ = 0;
    int switch_stack_ = 0;
    int func_def_stack_ = 0;

    // == Resolver Helpers ====================================================
    // ========================================================================

    void begin_scope()
    {
        scope_stack_.push_back(ScopeMap{});
    }

    void declare(NssToken token, Declaration* decl)
    {
        auto s = std::string(token.loc.view());
        auto it = scope_stack_.back().find(s);
        if (it != std::end(scope_stack_.back())) {
            if (dynamic_cast<FunctionDecl*>(it->second.decl)
                && dynamic_cast<FunctionDefinition*>(decl)) {
                it->second.decl = decl;
            } else {
                ctx_->semantic_error(parent_,
                    fmt::format("declaring '{}' in the same scope twice", token.loc.view()),
                    token.loc);
                return;
            }
        } else {
            scope_stack_.back().insert({s, {false, decl}});
        }
    }

    void define(NssToken token)
    {
        auto s = std::string(token.loc.view());
        auto it = scope_stack_.back().find(s);
        if (it == std::end(scope_stack_.back())) {
            ctx_->semantic_error(parent_,
                fmt::format("defining unknown variable '{}'", token.loc.view()),
                token.loc);
        }
        it->second.ready = true;
    }

    void end_scope()
    {
        scope_stack_.pop_back();
    }

    Declaration* locate(std::string_view token, Nss* script)
    {
        if (auto decl = script->locate_export(token)) {
            return decl;
        } else {
            for (auto& it : reverse(script->ast().includes)) {
                if (auto decl = locate(token, it)) {
                    return decl;
                }
            }
        }
        return nullptr;
    }

    Declaration* resolve(std::string_view token, SourceLocation loc)
    {
        auto s = std::string(token);

        // Look first through the scope stack in the current script
        for (const auto& map : reverse(scope_stack_)) {
            auto it = map.find(s);
            if (it == std::end(map)) { continue; }
            if (!it->second.ready) {
                ctx_->semantic_error(parent_,
                    fmt::format("using declared variable '{}' in init", token),
                    loc);
            }
            return it->second.decl;
        }

        // Next look through all dependencies
        for (auto it : reverse(parent_->ast().includes)) {
            if (auto decl = locate(token, it)) { return decl; }
        }

        if (parent_->name() != "nwscript") {
            auto nwscript = ctx_->get({"nwscript"}, ctx_);
            if (nwscript) {
                nwscript->resolve();
                return nwscript->locate_export(token);
            }
        }

        return nullptr;
    }

    // == Visitor =============================================================
    // ========================================================================

    virtual void visit(Ast* script) override
    {
        begin_scope();
        for (const auto& decl : script->decls) {
            decl->accept(this);
            if (auto d = dynamic_cast<VarDecl*>(decl.get())) {
                d->is_const_ = true; // All top level var decls are constant.  Only thing that makes sense.
                parent_->add_export(std::string(d->identifier.loc.view()), d);
            } else if (auto d = dynamic_cast<StructDecl*>(decl.get())) {
                parent_->add_export(std::string(d->type.struct_id.loc.view()), d);
            } else if (auto d = dynamic_cast<FunctionDecl*>(decl.get())) {
                parent_->add_export(std::string(d->identifier.loc.view()), d);
            } else if (auto d = dynamic_cast<FunctionDefinition*>(decl.get())) {
                parent_->add_export(std::string(d->decl->identifier.loc.view()), d);
            }
        }
        end_scope();
    }

    // Decls

    void match_function_decls(FunctionDecl* decl, FunctionDecl* def)
    {
        if (!decl || !def) { return; }

        // If there's a function declaration, try to match
        if (def->type_id_ != decl->type_id_) {
            ctx_->semantic_error(parent_,
                fmt::format("function declared with return type '{}', defined with return type '{}'",
                    ctx_->type_name(decl->type_id_),
                    ctx_->type_name(def->type_id_)));
        }

        if (decl->params.size() != def->params.size()) {
            ctx_->semantic_error(parent_,
                fmt::format("function declared with parameter count '{}', defined with parameter count '{}'",
                    decl->params.size(),
                    def->params.size()));
        } else {
            std::string reason;

            for (size_t i = 0; i < decl->params.size(); ++i) {
                SourceLocation loc;
                bool mismatch = false;
                bool warning = false;

                if (decl->params[i]->type_id_ != def->params[i]->type_id_) {
                    reason = fmt::format("function parameter declared with type '{}', defined with type '{}'",
                        ctx_->type_name(decl->params[i]->type_id_), ctx_->type_name(def->params[i]->type_id_));
                    mismatch = true;
                    loc = decl->params[i]->identifier.loc;
                } else if (decl->params[i]->identifier.loc.view() != def->params[i]->identifier.loc.view()) {
                    reason = fmt::format("function parameter declared with identifier '{}', defined with identifier '{}'",
                        decl->params[i]->identifier.loc.view(), def->params[i]->identifier.loc.view());
                    mismatch = true;
                    warning = true;
                    loc = decl->params[i]->identifier.loc;
                } else if (decl->params[i]->is_const_ != def->params[i]->is_const_) {
                    reason = fmt::format("function parameter const mistmatch",
                        ctx_->type_name(decl->params[i]->type_id_), ctx_->type_name(def->params[i]->type_id_));
                    mismatch = true;
                    loc = decl->params[i]->identifier.loc;
                } else if (decl->params[i]->init && def->params[i]->init) {
                    // [TODO] Probably need to have some sort of constant folding or tree walking interpreter
                    // to ensure the values of initializers are the same.
                    auto lit1 = dynamic_cast<LiteralExpression*>(decl->params[i]->init.get());
                    auto lit2 = dynamic_cast<LiteralExpression*>(def->params[i]->init.get());
                    if (lit1 && lit2 && lit1->data != lit2->data) {
                        reason = "mismatch parameter initializers";
                        mismatch = true;
                        loc = decl->params[i]->identifier.loc;
                    } else {
                        auto vlit1 = dynamic_cast<LiteralVectorExpression*>(decl->params[i]->init.get());
                        auto vlit2 = dynamic_cast<LiteralVectorExpression*>(def->params[i]->init.get());
                        if (vlit1 && vlit2 && vlit1->data != vlit2->data) {
                            reason = "mismatch parameter initializers";
                            mismatch = true;
                            loc = decl->params[i]->identifier.loc;
                        }
                    }
                }
                if (mismatch) {
                    if (warning) {
                        ctx_->semantic_warning(parent_, reason, loc);
                    } else {
                        ctx_->semantic_error(parent_, reason, loc);
                    }
                }
            }
        }
    }

    virtual void visit(FunctionDecl* decl) override
    {
        // Check to see if there's been a function definition, if so got to match.
        auto fd = resolve(decl->identifier.loc.view(), decl->identifier.loc);

        decl->type_id_ = ctx_->type_id(decl->type);
        declare(decl->identifier, decl);
        define(decl->identifier);

        begin_scope();
        for (auto& p : decl->params) {
            p->accept(this);
            if (p->init && !p->init->is_const_) {
                ctx_->semantic_error(parent_, "initializing parameter a with non-constant expression",
                    p->identifier.loc);
            }
        }
        end_scope();
        match_function_decls(decl, dynamic_cast<FunctionDecl*>(fd));
    }

    virtual void visit(FunctionDefinition* decl) override
    {
        ++func_def_stack_;
        // Check to see if there's been a function declaration, if so got to match.
        auto fd = resolve(decl->decl->identifier.loc.view(), decl->decl->identifier.loc);

        decl->type_id_ = decl->decl->type_id_ = ctx_->type_id(decl->decl->type);

        declare(decl->decl->identifier, decl);
        define(decl->decl->identifier);

        begin_scope();
        for (auto& p : decl->decl->params) {
            p->accept(this);
            if (p->init && !p->init->is_const_) {
                ctx_->semantic_error(parent_, "initializing parameter a with non-constant expression",
                    p->identifier.loc);
            }
        }

        match_function_decls(dynamic_cast<FunctionDecl*>(fd), decl->decl.get());

        decl->block->accept(this);
        end_scope();
        --func_def_stack_;
    }

    virtual void visit(StructDecl* decl) override
    {
        declare(decl->type.struct_id, decl);
        decl->type_id_ = ctx_->type_id(decl->type);
        begin_scope();
        for (auto& it : decl->decls) {
            it->accept(this);
        }
        end_scope();
        // Define down here so there's no recursive elements
        define(decl->type.struct_id);
    }

    virtual void visit(VarDecl* decl) override
    {
        decl->is_const_ = decl->type.type_qualifier.type == NssTokenType::CONST_;
        decl->type_id_ = ctx_->type_id(decl->type);

        if (decl->is_const_ && !decl->init) {
            ctx_->semantic_error(parent_, "constant variable declaration with no initializer");
        }

        declare(decl->identifier, decl);
        if (decl->init) {
            decl->init->accept(this);

            if (decl->type_id_ == ctx_->type_id("float")
                && decl->init->type_id_ == ctx_->type_id("int")) {
                // This is fine
            } else if (decl->type_id_ != decl->init->type_id_) {
                ctx_->semantic_error(parent_,
                    fmt::format("initializing variable '{}' of type '{}' with value of type '{}'",
                        decl->identifier.loc.view(),
                        ctx_->type_name(decl->type_id_),
                        ctx_->type_name(decl->init->type_id_)),
                    decl->identifier.loc);
            }
        }
        define(decl->identifier);
    }

    // Expressions
    virtual void visit(AssignExpression* expr) override
    {
        expr->lhs->accept(this);
        expr->rhs->accept(this);

        if (!ctx_->type_check_binary_op(expr->op, expr->lhs->type_id_, expr->rhs->type_id_)) {
            ctx_->semantic_error(parent_,
                fmt::format("invalid operands of types '{}' and '{}' to binary operator '{}'",
                    ctx_->type_name(expr->lhs->type_id_),
                    ctx_->type_name(expr->rhs->type_id_),
                    expr->op.loc.view()),
                expr->op.loc);
            return;
        }

        expr->type_id_ = expr->lhs->type_id_;
    }

    virtual void visit(BinaryExpression* expr) override
    {
        expr->lhs->accept(this);
        expr->rhs->accept(this);

        expr->is_const_ = expr->lhs->is_const_ && expr->rhs->is_const_;

        if (!ctx_->type_check_binary_op(expr->op, expr->lhs->type_id_, expr->rhs->type_id_)) {
            ctx_->semantic_error(parent_,
                fmt::format("invalid operands of types '{}' and '{}' to binary operator '{}'",
                    ctx_->type_name(expr->lhs->type_id_),
                    ctx_->type_name(expr->rhs->type_id_),
                    expr->op.loc.view()),
                expr->op.loc);
            return;
        }
        expr->type_id_ = expr->lhs->type_id_;
    }

    virtual void visit(CallExpression* expr) override
    {
        auto ve = dynamic_cast<VariableExpression*>(expr->expr.get());
        if (!ve) {
            // Parser already handles this case
            ctx_->semantic_error(parent_, "call expressions identifier is not variable expression");
            return;
        }

        FunctionDecl* func_decl = nullptr;
        auto decl = resolve(ve->var.loc.view(), ve->var.loc);
        if (auto fd = dynamic_cast<FunctionDecl*>(decl)) {
            func_decl = fd;
        } else if (auto fd = dynamic_cast<FunctionDefinition*>(decl)) {
            func_decl = fd->decl.get();
        } else {
            ctx_->semantic_error(parent_,
                fmt::format("unable to resolve identifier '{}'", ve->var.loc.view()),
                ve->extent());
            return;
        }

        expr->type_id_ = func_decl->type_id_;

        size_t req = 0;
        for (const auto& p : func_decl->params) {
            if (p->init) { break; }
            ++req;
        }

        if (expr->args.size() < req || expr->args.size() > func_decl->params.size()) {
            ctx_->semantic_error(parent_,
                fmt::format("no matching function call '{}' expected {} parameters", expr->extent().view(), req),
                expr->extent());
            return;
        }

        for (size_t i = 0; i < expr->args.size(); ++i) {
            expr->args[i]->accept(this);

            if (func_decl->params[i]->type_id_ == ctx_->type_id("float")
                && expr->args[i]->type_id_ == ctx_->type_id("int")) {
                // This is fine
            } else if (func_decl->params[i]->type_id_ == ctx_->type_id("action")
                && dynamic_cast<CallExpression*>(expr->args[i].get())) {
                // This is fine
            } else if (func_decl->params[i]->type_id_ != expr->args[i]->type_id_) {
                ctx_->semantic_error(parent_,
                    fmt::format("no matching function call '{}' expected parameter type '{}'",
                        expr->extent().view(),
                        ctx_->type_name(func_decl->params[i]->type_id_)),
                    expr->extent());
            }
        }
    }

    virtual void visit(ComparisonExpression* expr) override
    {
        expr->lhs->accept(this);
        expr->rhs->accept(this);

        expr->is_const_ = expr->lhs->is_const_ && expr->rhs->is_const_;

        if (expr->lhs->type_id_ != expr->rhs->type_id_
            && !ctx_->is_type_convertible(expr->lhs->type_id_, expr->rhs->type_id_)
            && !ctx_->is_type_convertible(expr->rhs->type_id_, expr->lhs->type_id_)) {
            ctx_->semantic_error(parent_,
                fmt::format("mismatched types in binary-expression '{}' != '{}', {}",
                    ctx_->type_name(expr->lhs->type_id_), ctx_->type_name(expr->rhs->type_id_), expr->extent().view()),
                expr->extent());
        }
        expr->type_id_ = ctx_->type_id("int");
    }

    virtual void visit(ConditionalExpression* expr) override
    {
        expr->test->accept(this);
        if (expr->test->type_id_ != ctx_->type_id("int")) {
            ctx_->semantic_error(parent_,
                fmt::format("could not convert value of type '{}' to integer bool",
                    ctx_->type_name(expr->test->type_id_)),
                expr->test->extent());
        }

        expr->true_branch->accept(this);
        expr->false_branch->accept(this);

        if (expr->true_branch->type_id_ != expr->false_branch->type_id_) {
            ctx_->semantic_error(parent_,
                fmt::format("operands of operator ?: have different types '{}' and '{}'",
                    ctx_->type_name(expr->true_branch->type_id_),
                    ctx_->type_name(expr->false_branch->type_id_)),
                expr->extent());
        }

        expr->type_id_ = expr->true_branch->type_id_;
    }

    virtual void visit(DotExpression* expr) override
    {
        auto resolve_struct_member = [this](VariableExpression* var, StructDecl* str) {
            for (const auto& it : str->decls) {
                if (it->identifier.loc.view() == var->var.loc.view()) {
                    var->type_id_ = it->type_id_;
                    var->is_const_ = it->is_const_;
                    return true;
                }
            }
            return false;
        };

        auto ex_rhs = dynamic_cast<VariableExpression*>(expr->rhs.get());
        if (!ex_rhs) {
            ctx_->semantic_error(parent_,
                "struct member must be a variable expression",
                expr->dot.loc);
            return;
        }

        StructDecl* struct_decl = nullptr;
        std::string_view struct_type;
        if (auto de = dynamic_cast<DotExpression*>(expr->lhs.get())) {
            expr->lhs->accept(this);
            struct_type = ctx_->type_name(expr->lhs->type_id_);
            struct_decl = struct_decl = dynamic_cast<StructDecl*>(resolve(struct_type, expr->dot.loc));
        } else if (auto ve = dynamic_cast<VariableExpression*>(expr->lhs.get())) {
            ve->accept(this);

            // special case vector lookup here for now
            if (ve->type_id_ == ctx_->type_id("vector")
                && (ex_rhs->var.loc.view() == "x"
                    || ex_rhs->var.loc.view() == "y"
                    || ex_rhs->var.loc.view() == "z")) {
                expr->type_id_ = ctx_->type_id("float");
                return;
            }

            struct_type = ctx_->type_name(ve->type_id_); // ve->var.loc.view();
            struct_decl = dynamic_cast<StructDecl*>(resolve(ctx_->type_name(ve->type_id_), ve->var.loc));
        }

        if (!struct_decl) {
            ctx_->semantic_error(parent_,
                fmt::format("request for member '{}' in '{}', which is of non-struct type",
                    ex_rhs->var.loc.view(), struct_type),
                expr->dot.loc);
        } else if (!resolve_struct_member(ex_rhs, struct_decl)) {
            ctx_->semantic_error(parent_,
                fmt::format("request for member '{}', which is not in struct of type '{}'",
                    ex_rhs->var.loc.view(), struct_type),
                expr->dot.loc);
        }

        expr->type_id_ = expr->rhs->type_id_;
    }

    virtual void visit(GroupingExpression* expr) override
    {
        expr->expr->accept(this);
        expr->type_id_ = expr->expr->type_id_;
        expr->is_const_ = expr->expr->is_const_;
    }

    virtual void visit(LiteralExpression* expr) override
    {
        expr->is_const_ = true;
        if (expr->literal.type == NssTokenType::FLOAT_CONST) {
            expr->type_id_ = ctx_->type_id("float");
        } else if (expr->literal.type == NssTokenType::INTEGER_CONST) {
            expr->type_id_ = ctx_->type_id("int");
        } else if (expr->literal.type == NssTokenType::STRING_CONST) {
            expr->type_id_ = ctx_->type_id("string");
        } else if (expr->literal.type == NssTokenType::OBJECT_SELF_CONST
            || expr->literal.type == NssTokenType::OBJECT_INVALID_CONST) {
            expr->type_id_ = ctx_->type_id("object");
        }
    }

    virtual void visit(LiteralVectorExpression* expr) override
    {
        expr->is_const_ = true;
        expr->type_id_ = ctx_->type_id("vector");
    }

    virtual void visit(LogicalExpression* expr) override
    {
        expr->lhs->accept(this);
        expr->rhs->accept(this);

        if (expr->lhs->type_id_ != expr->rhs->type_id_) {
            ctx_->semantic_error(parent_, "mismatched types", {});
        }

        expr->type_id_ = ctx_->type_id("int");
        expr->is_const_ = expr->lhs->is_const_ && expr->rhs->is_const_;
    }

    virtual void visit(PostfixExpression* expr) override
    {
        expr->lhs->accept(this);
        expr->type_id_ = expr->lhs->type_id_;
        expr->is_const_ = expr->lhs->is_const_;
    }

    virtual void visit(UnaryExpression* expr) override
    {
        expr->rhs->accept(this);
        expr->type_id_ = expr->rhs->type_id_;
        expr->is_const_ = expr->rhs->is_const_;
    }

    virtual void visit(VariableExpression* expr) override
    {
        auto decl = resolve(expr->var.loc.view(), expr->var.loc);
        if (decl) {
            expr->type_id_ = decl->type_id_;
            expr->is_const_ = decl->is_const_;
        } else {
            ctx_->semantic_error(parent_,
                fmt::format("unable to resolve identifier '{}'", expr->var.loc.view()),
                expr->extent());
        }
    }

    // Statements
    virtual void visit(BlockStatement* stmt) override
    {
        stmt->type_id_ = ctx_->type_id("void");
        for (auto& s : stmt->nodes) {
            s->accept(this);
        }
    }

    virtual void visit(DeclStatement* stmt) override
    {
        size_t ti = invalid_type_id;
        for (auto& s : stmt->decls) {
            // types of all must be the same;
            s->accept(this);
            if (ti == invalid_type_id) {
                ti = s->type_id_;
            } else {
                if (ti != s->type_id_) {
                }
            }
        }
    }

    virtual void visit(DoStatement* stmt) override
    {
        ++loop_stack_;
        begin_scope();
        stmt->block->accept(this);
        end_scope();

        stmt->expr->accept(this);
        if (stmt->expr->type_id_ != ctx_->type_id("int")) {
            ctx_->semantic_error(parent_,
                fmt::format("could not convert value of type '{}' to integer bool",
                    ctx_->type_name(stmt->expr->type_id_)),
                stmt->expr->extent());
        }

        --loop_stack_;
    }

    virtual void visit(EmptyStatement* stmt) override
    {
        stmt->type_id_ = ctx_->type_id("void");
    }

    virtual void visit(ExprStatement* stmt) override
    {
        stmt->expr->accept(this);
    }

    virtual void visit(IfStatement* stmt) override
    {
        stmt->type_id_ = ctx_->type_id("void");
        stmt->expr->accept(this);

        if (stmt->expr->type_id_ != ctx_->type_id("int")) {
            ctx_->semantic_error(parent_,
                fmt::format("could not convert value of type '{}' to integer bool",
                    ctx_->type_name(stmt->expr->type_id_)),
                stmt->expr->extent());
        }

        begin_scope();
        stmt->if_branch->accept(this);
        end_scope();
        if (stmt->else_branch) {
            begin_scope();
            stmt->else_branch->accept(this);
            end_scope();
        }
    }

    virtual void visit(ForStatement* stmt) override
    {
        ++loop_stack_;
        begin_scope();

        if (stmt->init) {
            stmt->init->accept(this);
        }

        if (stmt->check) {
            stmt->check->accept(this);
            if (stmt->check->type_id_ != ctx_->type_id("int")) {
                ctx_->semantic_error(parent_,
                    fmt::format("could not convert value of type '{}' to integer bool",
                        ctx_->type_name(stmt->check->type_id_)),
                    stmt->check->extent());
            }
        }

        if (stmt->inc) {
            stmt->inc->accept(this);
        }

        stmt->block->accept(this);
        end_scope();
        --loop_stack_;
    }

    virtual void visit(JumpStatement* stmt) override
    {
        if (stmt->expr) {
            stmt->expr->accept(this);
            stmt->type_id_ = stmt->expr->type_id_;
        } else {
            stmt->type_id_ = ctx_->type_id("void");
        }

        if (stmt->op.type == NssTokenType::CONTINUE
            && loop_stack_ == 0) {
            ctx_->semantic_error(parent_, "continue statement not within a loop", stmt->op.loc);
        } else if (stmt->op.type == NssTokenType::BREAK
            && (loop_stack_ == 0 && switch_stack_ == 0)) {
            ctx_->semantic_error(parent_, "break statement not within loop or switch", stmt->op.loc);
        } else if (stmt->op.type == NssTokenType::RETURN && func_def_stack_ == 0) {
            // This shouldn't even be possible and would be a parser error
            ctx_->semantic_error(parent_, "return statement not within function definition", stmt->op.loc);
        }
    }

    virtual void visit(LabelStatement* stmt) override
    {
        if (stmt->type.type == NssTokenType::CASE && switch_stack_ == 0) {
            ctx_->semantic_error(parent_, "case statement not within switch", stmt->type.loc);
        }

        if (stmt->type.type == NssTokenType::DEFAULT) {
            return; // No expr..
        }

        stmt->expr->accept(this);
        if (stmt->expr->type_id_ != ctx_->type_id("int")
            && stmt->expr->type_id_ != ctx_->type_id("string")) {
            ctx_->semantic_error(parent_,
                fmt::format("could not convert value to integer or string"));
        } else if (!stmt->expr->is_const_) {
            ctx_->semantic_error(parent_, "case expression must be constant expression");
        }
    }

    virtual void visit(SwitchStatement* stmt) override
    {
        stmt->type_id_ = ctx_->type_id("void");
        ++switch_stack_;
        stmt->target->accept(this);

        // this could have string type also, but when the string case statements
        // were added to NWscript, the NWN:EE team half-assed this from what
        // I could tell.
        if (stmt->target->type_id_ != ctx_->type_id("int")) {
            ctx_->semantic_error(parent_,
                fmt::format("switch quantity not an integer"),
                stmt->target->extent());
        }

        begin_scope();
        stmt->block->accept(this);
        end_scope();
        --switch_stack_;
    }

    virtual void visit(WhileStatement* stmt) override
    {
        stmt->type_id_ = ctx_->type_id("void");
        ++loop_stack_;

        stmt->check->accept(this);
        if (stmt->check->type_id_ != ctx_->type_id("int")) {
            ctx_->semantic_error(parent_,
                fmt::format("could not convert value of type '{}' to integer bool",
                    ctx_->type_name(stmt->check->type_id_)),
                stmt->check->extent());
        }

        begin_scope();
        stmt->block->accept(this);
        end_scope();
        --loop_stack_;
    }
};

} // namespace nw::script
