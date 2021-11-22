# Generated from DND.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2=\2\27\3")
        buf.write("\2\2\2\4\32\3\2\2\2\6 \3\2\2\2\b(\3\2\2\2\n,\3\2\2\2\f")
        buf.write("\60\3\2\2\2\16\64\3\2\2\2\208\3\2\2\2\22=\3\2\2\2\24\26")
        buf.write("\5\4\3\2\25\24\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27")
        buf.write("\30\3\2\2\2\30\3\3\2\2\2\31\27\3\2\2\2\32\33\7\3\2\2\33")
        buf.write("\34\7\31\2\2\34\35\7\4\2\2\35\36\5\6\4\2\36\37\7\5\2\2")
        buf.write("\37\5\3\2\2\2 !\5\b\5\2!\"\7\6\2\2\"#\5\n\6\2#$\7\6\2")
        buf.write("\2$%\5\f\7\2%&\7\6\2\2&\'\5\16\b\2\'\7\3\2\2\2()\7\7\2")
        buf.write("\2)*\7\25\2\2*+\7\17\2\2+\t\3\2\2\2,-\7\b\2\2-.\7\25\2")
        buf.write("\2./\7\21\2\2/\13\3\2\2\2\60\61\7\t\2\2\61\62\7\25\2\2")
        buf.write("\62\63\7\27\2\2\63\r\3\2\2\2\64\65\7\n\2\2\65\66\7\25")
        buf.write("\2\2\66\67\7\21\2\2\67\17\3\2\2\289\7\13\2\29:\7\25\2")
        buf.write("\2:;\7\17\2\2;<\7\30\2\2<\21\3\2\2\2=>\7\f\2\2>?\7\25")
        buf.write("\2\2?@\7\r\2\2@A\7\17\2\2AB\7\6\2\2BC\7\26\2\2CD\7\16")
        buf.write("\2\2D\23\3\2\2\2\3\27")
        return buf.getvalue()


class DNDParser ( Parser ):

    grammarFileName = "DND.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'{'", "'}'", "','", "'LEVEL'", 
                     "'NAME'", "'SCHOOL'", "'DESCR'", "'DAMAGE'", "'CAST'", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM_INT", "NUM_REAL", "STRING", "OPEN_STRING", 
                      "COMMENT", "WS", "SEP", "CAST_TIME", "SCHOOL", "DICE", 
                      "IDENT" ]

    RULE_program = 0
    RULE_spell = 1
    RULE_tags = 2
    RULE_level_tag = 3
    RULE_name_tag = 4
    RULE_school_tag = 5
    RULE_descr_tag = 6
    RULE_damage_tag = 7
    RULE_cast_tag = 8

    ruleNames =  [ "program", "spell", "tags", "level_tag", "name_tag", 
                   "school_tag", "descr_tag", "damage_tag", "cast_tag" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    NUM_INT=13
    NUM_REAL=14
    STRING=15
    OPEN_STRING=16
    COMMENT=17
    WS=18
    SEP=19
    CAST_TIME=20
    SCHOOL=21
    DICE=22
    IDENT=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spell(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DNDParser.SpellContext)
            else:
                return self.getTypedRuleContext(DNDParser.SpellContext,i)


        def getRuleIndex(self):
            return DNDParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DNDParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DNDParser.T__0:
                self.state = 18
                self.spell()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SpellContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(DNDParser.IDENT, 0)

        def tags(self):
            return self.getTypedRuleContext(DNDParser.TagsContext,0)


        def getRuleIndex(self):
            return DNDParser.RULE_spell

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpell" ):
                listener.enterSpell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpell" ):
                listener.exitSpell(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpell" ):
                return visitor.visitSpell(self)
            else:
                return visitor.visitChildren(self)




    def spell(self):

        localctx = DNDParser.SpellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_spell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(DNDParser.T__0)
            self.state = 25
            self.match(DNDParser.IDENT)
            self.state = 26
            self.match(DNDParser.T__1)
            self.state = 27
            self.tags()
            self.state = 28
            self.match(DNDParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TagsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def level_tag(self):
            return self.getTypedRuleContext(DNDParser.Level_tagContext,0)


        def name_tag(self):
            return self.getTypedRuleContext(DNDParser.Name_tagContext,0)


        def school_tag(self):
            return self.getTypedRuleContext(DNDParser.School_tagContext,0)


        def descr_tag(self):
            return self.getTypedRuleContext(DNDParser.Descr_tagContext,0)


        def getRuleIndex(self):
            return DNDParser.RULE_tags

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTags" ):
                listener.enterTags(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTags" ):
                listener.exitTags(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTags" ):
                return visitor.visitTags(self)
            else:
                return visitor.visitChildren(self)




    def tags(self):

        localctx = DNDParser.TagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tags)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.level_tag()
            self.state = 31
            self.match(DNDParser.T__3)
            self.state = 32
            self.name_tag()
            self.state = 33
            self.match(DNDParser.T__3)
            self.state = 34
            self.school_tag()
            self.state = 35
            self.match(DNDParser.T__3)
            self.state = 36
            self.descr_tag()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Level_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP(self):
            return self.getToken(DNDParser.SEP, 0)

        def NUM_INT(self):
            return self.getToken(DNDParser.NUM_INT, 0)

        def getRuleIndex(self):
            return DNDParser.RULE_level_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLevel_tag" ):
                listener.enterLevel_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLevel_tag" ):
                listener.exitLevel_tag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLevel_tag" ):
                return visitor.visitLevel_tag(self)
            else:
                return visitor.visitChildren(self)




    def level_tag(self):

        localctx = DNDParser.Level_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_level_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(DNDParser.T__4)
            self.state = 39
            self.match(DNDParser.SEP)
            self.state = 40
            self.match(DNDParser.NUM_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Name_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP(self):
            return self.getToken(DNDParser.SEP, 0)

        def STRING(self):
            return self.getToken(DNDParser.STRING, 0)

        def getRuleIndex(self):
            return DNDParser.RULE_name_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_tag" ):
                listener.enterName_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_tag" ):
                listener.exitName_tag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_tag" ):
                return visitor.visitName_tag(self)
            else:
                return visitor.visitChildren(self)




    def name_tag(self):

        localctx = DNDParser.Name_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_name_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(DNDParser.T__5)
            self.state = 43
            self.match(DNDParser.SEP)
            self.state = 44
            self.match(DNDParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class School_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP(self):
            return self.getToken(DNDParser.SEP, 0)

        def SCHOOL(self):
            return self.getToken(DNDParser.SCHOOL, 0)

        def getRuleIndex(self):
            return DNDParser.RULE_school_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchool_tag" ):
                listener.enterSchool_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchool_tag" ):
                listener.exitSchool_tag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSchool_tag" ):
                return visitor.visitSchool_tag(self)
            else:
                return visitor.visitChildren(self)




    def school_tag(self):

        localctx = DNDParser.School_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_school_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(DNDParser.T__6)
            self.state = 47
            self.match(DNDParser.SEP)
            self.state = 48
            self.match(DNDParser.SCHOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Descr_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP(self):
            return self.getToken(DNDParser.SEP, 0)

        def STRING(self):
            return self.getToken(DNDParser.STRING, 0)

        def getRuleIndex(self):
            return DNDParser.RULE_descr_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescr_tag" ):
                listener.enterDescr_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescr_tag" ):
                listener.exitDescr_tag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDescr_tag" ):
                return visitor.visitDescr_tag(self)
            else:
                return visitor.visitChildren(self)




    def descr_tag(self):

        localctx = DNDParser.Descr_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_descr_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(DNDParser.T__7)
            self.state = 51
            self.match(DNDParser.SEP)
            self.state = 52
            self.match(DNDParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Damage_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP(self):
            return self.getToken(DNDParser.SEP, 0)

        def NUM_INT(self):
            return self.getToken(DNDParser.NUM_INT, 0)

        def DICE(self):
            return self.getToken(DNDParser.DICE, 0)

        def getRuleIndex(self):
            return DNDParser.RULE_damage_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDamage_tag" ):
                listener.enterDamage_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDamage_tag" ):
                listener.exitDamage_tag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDamage_tag" ):
                return visitor.visitDamage_tag(self)
            else:
                return visitor.visitChildren(self)




    def damage_tag(self):

        localctx = DNDParser.Damage_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_damage_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(DNDParser.T__8)
            self.state = 55
            self.match(DNDParser.SEP)

            self.state = 56
            self.match(DNDParser.NUM_INT)
            self.state = 57
            self.match(DNDParser.DICE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cast_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP(self):
            return self.getToken(DNDParser.SEP, 0)

        def NUM_INT(self):
            return self.getToken(DNDParser.NUM_INT, 0)

        def CAST_TIME(self):
            return self.getToken(DNDParser.CAST_TIME, 0)

        def getRuleIndex(self):
            return DNDParser.RULE_cast_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCast_tag" ):
                listener.enterCast_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCast_tag" ):
                listener.exitCast_tag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCast_tag" ):
                return visitor.visitCast_tag(self)
            else:
                return visitor.visitChildren(self)




    def cast_tag(self):

        localctx = DNDParser.Cast_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cast_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(DNDParser.T__9)
            self.state = 60
            self.match(DNDParser.SEP)
            self.state = 61
            self.match(DNDParser.T__10)
            self.state = 62
            self.match(DNDParser.NUM_INT)
            self.state = 63
            self.match(DNDParser.T__3)
            self.state = 64
            self.match(DNDParser.CAST_TIME)
            self.state = 65
            self.match(DNDParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





