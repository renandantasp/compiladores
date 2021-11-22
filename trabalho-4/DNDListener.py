# Generated from DND.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DNDParser import DNDParser
else:
    from DNDParser import DNDParser

# This class defines a complete listener for a parse tree produced by DNDParser.
class DNDListener(ParseTreeListener):

    # Enter a parse tree produced by DNDParser#program.
    def enterProgram(self, ctx:DNDParser.ProgramContext):
        pass

    # Exit a parse tree produced by DNDParser#program.
    def exitProgram(self, ctx:DNDParser.ProgramContext):
        pass


    # Enter a parse tree produced by DNDParser#spell.
    def enterSpell(self, ctx:DNDParser.SpellContext):
        pass

    # Exit a parse tree produced by DNDParser#spell.
    def exitSpell(self, ctx:DNDParser.SpellContext):
        pass


    # Enter a parse tree produced by DNDParser#tags.
    def enterTags(self, ctx:DNDParser.TagsContext):
        pass

    # Exit a parse tree produced by DNDParser#tags.
    def exitTags(self, ctx:DNDParser.TagsContext):
        pass


    # Enter a parse tree produced by DNDParser#level_tag.
    def enterLevel_tag(self, ctx:DNDParser.Level_tagContext):
        pass

    # Exit a parse tree produced by DNDParser#level_tag.
    def exitLevel_tag(self, ctx:DNDParser.Level_tagContext):
        pass


    # Enter a parse tree produced by DNDParser#name_tag.
    def enterName_tag(self, ctx:DNDParser.Name_tagContext):
        pass

    # Exit a parse tree produced by DNDParser#name_tag.
    def exitName_tag(self, ctx:DNDParser.Name_tagContext):
        pass


    # Enter a parse tree produced by DNDParser#school_tag.
    def enterSchool_tag(self, ctx:DNDParser.School_tagContext):
        pass

    # Exit a parse tree produced by DNDParser#school_tag.
    def exitSchool_tag(self, ctx:DNDParser.School_tagContext):
        pass


    # Enter a parse tree produced by DNDParser#descr_tag.
    def enterDescr_tag(self, ctx:DNDParser.Descr_tagContext):
        pass

    # Exit a parse tree produced by DNDParser#descr_tag.
    def exitDescr_tag(self, ctx:DNDParser.Descr_tagContext):
        pass


    # Enter a parse tree produced by DNDParser#damage_tag.
    def enterDamage_tag(self, ctx:DNDParser.Damage_tagContext):
        pass

    # Exit a parse tree produced by DNDParser#damage_tag.
    def exitDamage_tag(self, ctx:DNDParser.Damage_tagContext):
        pass


    # Enter a parse tree produced by DNDParser#cast_tag.
    def enterCast_tag(self, ctx:DNDParser.Cast_tagContext):
        pass

    # Exit a parse tree produced by DNDParser#cast_tag.
    def exitCast_tag(self, ctx:DNDParser.Cast_tagContext):
        pass


