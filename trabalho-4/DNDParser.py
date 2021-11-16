# Generated from DND.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\7\3\32\n\3")
        buf.write("\f\3\16\3\35\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\5\13H\n\13\3\13\3\13\3\13\2\2")
        buf.write("\f\2\4\6\b\n\f\16\20\22\24\2\2\2C\2\26\3\2\2\2\4\33\3")
        buf.write("\2\2\2\6\36\3\2\2\2\b$\3\2\2\2\n,\3\2\2\2\f\60\3\2\2\2")
        buf.write("\16\64\3\2\2\2\208\3\2\2\2\22<\3\2\2\2\24D\3\2\2\2\26")
        buf.write("\27\5\4\3\2\27\3\3\2\2\2\30\32\5\6\4\2\31\30\3\2\2\2\32")
        buf.write("\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\5\3\2\2\2\35")
        buf.write("\33\3\2\2\2\36\37\7\3\2\2\37 \7\31\2\2 !\7\4\2\2!\"\5")
        buf.write("\b\5\2\"#\7\5\2\2#\7\3\2\2\2$%\5\n\6\2%&\7\6\2\2&\'\5")
        buf.write("\f\7\2\'(\7\6\2\2()\5\16\b\2)*\7\6\2\2*+\5\20\t\2+\t\3")
        buf.write("\2\2\2,-\7\7\2\2-.\7\26\2\2./\7\17\2\2/\13\3\2\2\2\60")
        buf.write("\61\7\b\2\2\61\62\7\26\2\2\62\63\7\21\2\2\63\r\3\2\2\2")
        buf.write("\64\65\7\t\2\2\65\66\7\26\2\2\66\67\7\30\2\2\67\17\3\2")
        buf.write("\2\289\7\n\2\29:\7\26\2\2:;\7\21\2\2;\21\3\2\2\2<=\7\13")
        buf.write("\2\2=>\7\26\2\2>?\7\f\2\2?@\7\17\2\2@A\7\6\2\2AB\7\27")
        buf.write("\2\2BC\7\r\2\2C\23\3\2\2\2DE\7\16\2\2EG\7\26\2\2FH\7\20")
        buf.write("\2\2GF\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\7\21\2\2J\25\3\2")
        buf.write("\2\2\4\33G")
        return buf.getvalue()


class DNDParser ( Parser ):

    grammarFileName = "DND.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'{'", "'}'", "','", "'LEVEL'", 
                     "'NAME'", "'SCHOOL'", "'DESCR'", "'CAST'", "'('", "')'", 
                     "'RANGE'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM_INT", "NUM_REAL", "STRING", "OPEN_STRING", 
                      "COMENT", "COMENT_ABERTO", "WS", "SEP", "CAST_TIME", 
                      "SCHOOL", "IDENT" ]

    RULE_program = 0
    RULE_body = 1
    RULE_spell = 2
    RULE_tags = 3
    RULE_level_tag = 4
    RULE_name_tag = 5
    RULE_school_tag = 6
    RULE_descr_tag = 7
    RULE_cast_tag = 8
    RULE_range_tag = 9

    ruleNames =  [ "program", "body", "spell", "tags", "level_tag", "name_tag", 
                   "school_tag", "descr_tag", "cast_tag", "range_tag" ]

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
    COMENT=17
    COMENT_ABERTO=18
    WS=19
    SEP=20
    CAST_TIME=21
    SCHOOL=22
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

        def body(self):
            return self.getTypedRuleContext(DNDParser.BodyContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spell(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DNDParser.SpellContext)
            else:
                return self.getTypedRuleContext(DNDParser.SpellContext,i)


        def getRuleIndex(self):
            return DNDParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = DNDParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DNDParser.T__0:
                self.state = 22
                self.spell()
                self.state = 27
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
        self.enterRule(localctx, 4, self.RULE_spell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(DNDParser.T__0)
            self.state = 29
            self.match(DNDParser.IDENT)
            self.state = 30
            self.match(DNDParser.T__1)

            self.state = 31
            self.tags()
            self.state = 32
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
        self.enterRule(localctx, 6, self.RULE_tags)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.level_tag()
            self.state = 35
            self.match(DNDParser.T__3)
            self.state = 36
            self.name_tag()
            self.state = 37
            self.match(DNDParser.T__3)
            self.state = 38
            self.school_tag()
            self.state = 39
            self.match(DNDParser.T__3)
            self.state = 40
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
        self.enterRule(localctx, 8, self.RULE_level_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(DNDParser.T__4)
            self.state = 43
            self.match(DNDParser.SEP)
            self.state = 44
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
        self.enterRule(localctx, 10, self.RULE_name_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(DNDParser.T__5)
            self.state = 47
            self.match(DNDParser.SEP)
            self.state = 48
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
        self.enterRule(localctx, 12, self.RULE_school_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(DNDParser.T__6)
            self.state = 51
            self.match(DNDParser.SEP)
            self.state = 52
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
        self.enterRule(localctx, 14, self.RULE_descr_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(DNDParser.T__7)
            self.state = 55
            self.match(DNDParser.SEP)
            self.state = 56
            self.match(DNDParser.STRING)
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
            self.state = 58
            self.match(DNDParser.T__8)
            self.state = 59
            self.match(DNDParser.SEP)
            self.state = 60
            self.match(DNDParser.T__9)
            self.state = 61
            self.match(DNDParser.NUM_INT)
            self.state = 62
            self.match(DNDParser.T__3)
            self.state = 63
            self.match(DNDParser.CAST_TIME)
            self.state = 64
            self.match(DNDParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_tagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP(self):
            return self.getToken(DNDParser.SEP, 0)

        def STRING(self):
            return self.getToken(DNDParser.STRING, 0)

        def NUM_REAL(self):
            return self.getToken(DNDParser.NUM_REAL, 0)

        def getRuleIndex(self):
            return DNDParser.RULE_range_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_tag" ):
                listener.enterRange_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_tag" ):
                listener.exitRange_tag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_tag" ):
                return visitor.visitRange_tag(self)
            else:
                return visitor.visitChildren(self)




    def range_tag(self):

        localctx = DNDParser.Range_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_range_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(DNDParser.T__11)
            self.state = 67
            self.match(DNDParser.SEP)

            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DNDParser.NUM_REAL:
                self.state = 68
                self.match(DNDParser.NUM_REAL)


            self.state = 71
            self.match(DNDParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





