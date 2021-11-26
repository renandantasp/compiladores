# Generated from DND.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DNDParser import DNDParser
else:
    from DNDParser import DNDParser

# This class defines a complete generic visitor for a parse tree produced by DNDParser.

class DNDVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DNDParser#program.
    def visitProgram(self, ctx:DNDParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#declaracao.
    def visitDeclaracao(self, ctx:DNDParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#decl.
    def visitDecl(self, ctx:DNDParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#spell.
    def visitSpell(self, ctx:DNDParser.SpellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#tags.
    def visitTags(self, ctx:DNDParser.TagsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#level_tag.
    def visitLevel_tag(self, ctx:DNDParser.Level_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#name_tag.
    def visitName_tag(self, ctx:DNDParser.Name_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#school_tag.
    def visitSchool_tag(self, ctx:DNDParser.School_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#descr_tag.
    def visitDescr_tag(self, ctx:DNDParser.Descr_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#opt_tags.
    def visitOpt_tags(self, ctx:DNDParser.Opt_tagsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#damage_tag.
    def visitDamage_tag(self, ctx:DNDParser.Damage_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#cast_tag.
    def visitCast_tag(self, ctx:DNDParser.Cast_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#damage_type_tag.
    def visitDamage_type_tag(self, ctx:DNDParser.Damage_type_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#comp_tag.
    def visitComp_tag(self, ctx:DNDParser.Comp_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#comp1.
    def visitComp1(self, ctx:DNDParser.Comp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#comp2.
    def visitComp2(self, ctx:DNDParser.Comp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#comp3.
    def visitComp3(self, ctx:DNDParser.Comp3Context):
        return self.visitChildren(ctx)



del DNDParser