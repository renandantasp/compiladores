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


    # Visit a parse tree produced by DNDParser#damage_tag.
    def visitDamage_tag(self, ctx:DNDParser.Damage_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DNDParser#cast_tag.
    def visitCast_tag(self, ctx:DNDParser.Cast_tagContext):
        return self.visitChildren(ctx)



del DNDParser