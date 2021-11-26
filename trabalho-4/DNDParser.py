# Generated from DND.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\7\2\31\n\2\f\2")
        buf.write("\16\2\34\13\2\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3\3\3\5\3")
        buf.write("&\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\5\13R\n\13\3\13\2\2\f\2\4\6\b\n\f\16")
        buf.write("\20\22\24\2\6\4\2\17\17\21\21\4\2\17\17\32\32\4\2\21\21")
        buf.write("\32\32\4\2\27\27\32\32\2M\2\26\3\2\2\2\4%\3\2\2\2\6\'")
        buf.write("\3\2\2\2\b-\3\2\2\2\n\63\3\2\2\2\f;\3\2\2\2\16?\3\2\2")
        buf.write("\2\20C\3\2\2\2\22G\3\2\2\2\24K\3\2\2\2\26\32\5\4\3\2\27")
        buf.write("\31\5\b\5\2\30\27\3\2\2\2\31\34\3\2\2\2\32\30\3\2\2\2")
        buf.write("\32\33\3\2\2\2\33\3\3\2\2\2\34\32\3\2\2\2\35!\7\3\2\2")
        buf.write("\36 \5\6\4\2\37\36\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3")
        buf.write("\2\2\2\"&\3\2\2\2#!\3\2\2\2$&\3\2\2\2%\35\3\2\2\2%$\3")
        buf.write("\2\2\2&\5\3\2\2\2\'(\7\30\2\2()\7\32\2\2)*\7\4\2\2*+\t")
        buf.write("\2\2\2+,\7\5\2\2,\7\3\2\2\2-.\7\6\2\2./\7\32\2\2/\60\7")
        buf.write("\7\2\2\60\61\5\n\6\2\61\62\7\b\2\2\62\t\3\2\2\2\63\64")
        buf.write("\5\f\7\2\64\65\7\t\2\2\65\66\5\16\b\2\66\67\7\t\2\2\67")
        buf.write("8\5\20\t\289\7\t\2\29:\5\22\n\2:\13\3\2\2\2;<\7\n\2\2")
        buf.write("<=\7\25\2\2=>\t\3\2\2>\r\3\2\2\2?@\7\13\2\2@A\7\25\2\2")
        buf.write("AB\t\4\2\2B\17\3\2\2\2CD\7\f\2\2DE\7\25\2\2EF\t\5\2\2")
        buf.write("F\21\3\2\2\2GH\7\r\2\2HI\7\25\2\2IJ\t\4\2\2J\23\3\2\2")
        buf.write("\2KL\7\16\2\2LQ\7\25\2\2MN\7\17\2\2NR\7\31\2\2OP\7\32")
        buf.write("\2\2PR\7\31\2\2QM\3\2\2\2QO\3\2\2\2R\25\3\2\2\2\6\32!")
        buf.write("%Q")
        return buf.getvalue()


class DNDParser ( Parser ):

    grammarFileName = "DND.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'decl:'", "'='", "';'", "'def'", "'{'", 
                     "'}'", "','", "'LEVEL'", "'NAME'", "'SCHOOL'", "'DESCR'", 
                     "'DAMAGE'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM_INT", "NUM_REAL", "STRING", "OPEN_STRING", 
                      "COMMENT", "WS", "SEP", "CAST_TIME", "SCHOOL", "DECL_TYPE", 
                      "DICE", "IDENT" ]

    RULE_program = 0
    RULE_declaracao = 1
    RULE_decl = 2
    RULE_spell = 3
    RULE_tags = 4
    RULE_level_tag = 5
    RULE_name_tag = 6
    RULE_school_tag = 7
    RULE_descr_tag = 8
    RULE_damage_tag = 9

    ruleNames =  [ "program", "declaracao", "decl", "spell", "tags", "level_tag", 
                   "name_tag", "school_tag", "descr_tag", "damage_tag" ]

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
    DECL_TYPE=22
    DICE=23
    IDENT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao(self):
            return self.getTypedRuleContext(DNDParser.DeclaracaoContext,0)


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
            self.state = 20
            self.declaracao()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DNDParser.T__3:
                self.state = 21
                self.spell()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DNDParser.DeclContext)
            else:
                return self.getTypedRuleContext(DNDParser.DeclContext,i)


        def getRuleIndex(self):
            return DNDParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = DNDParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracao)
        self._la = 0 # Token type
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DNDParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(DNDParser.T__0)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DNDParser.DECL_TYPE:
                    self.state = 28
                    self.decl()
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [DNDParser.EOF, DNDParser.T__3]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECL_TYPE(self):
            return self.getToken(DNDParser.DECL_TYPE, 0)

        def IDENT(self):
            return self.getToken(DNDParser.IDENT, 0)

        def STRING(self):
            return self.getToken(DNDParser.STRING, 0)

        def NUM_INT(self):
            return self.getToken(DNDParser.NUM_INT, 0)

        def getRuleIndex(self):
            return DNDParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = DNDParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(DNDParser.DECL_TYPE)
            self.state = 38
            self.match(DNDParser.IDENT)
            self.state = 39
            self.match(DNDParser.T__1)
            self.state = 40
            _la = self._input.LA(1)
            if not(_la==DNDParser.NUM_INT or _la==DNDParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 41
            self.match(DNDParser.T__2)
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
        self.enterRule(localctx, 6, self.RULE_spell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(DNDParser.T__3)
            self.state = 44
            self.match(DNDParser.IDENT)
            self.state = 45
            self.match(DNDParser.T__4)
            self.state = 46
            self.tags()
            self.state = 47
            self.match(DNDParser.T__5)
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
        self.enterRule(localctx, 8, self.RULE_tags)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.level_tag()
            self.state = 50
            self.match(DNDParser.T__6)
            self.state = 51
            self.name_tag()
            self.state = 52
            self.match(DNDParser.T__6)
            self.state = 53
            self.school_tag()
            self.state = 54
            self.match(DNDParser.T__6)
            self.state = 55
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

        def IDENT(self):
            return self.getToken(DNDParser.IDENT, 0)

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
        self.enterRule(localctx, 10, self.RULE_level_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(DNDParser.T__7)
            self.state = 58
            self.match(DNDParser.SEP)
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==DNDParser.NUM_INT or _la==DNDParser.IDENT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def IDENT(self):
            return self.getToken(DNDParser.IDENT, 0)

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
        self.enterRule(localctx, 12, self.RULE_name_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(DNDParser.T__8)
            self.state = 62
            self.match(DNDParser.SEP)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==DNDParser.STRING or _la==DNDParser.IDENT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def IDENT(self):
            return self.getToken(DNDParser.IDENT, 0)

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
        self.enterRule(localctx, 14, self.RULE_school_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(DNDParser.T__9)
            self.state = 66
            self.match(DNDParser.SEP)
            self.state = 67
            _la = self._input.LA(1)
            if not(_la==DNDParser.SCHOOL or _la==DNDParser.IDENT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def IDENT(self):
            return self.getToken(DNDParser.IDENT, 0)

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
        self.enterRule(localctx, 16, self.RULE_descr_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(DNDParser.T__10)
            self.state = 70
            self.match(DNDParser.SEP)
            self.state = 71
            _la = self._input.LA(1)
            if not(_la==DNDParser.STRING or _la==DNDParser.IDENT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def IDENT(self):
            return self.getToken(DNDParser.IDENT, 0)

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
        self.enterRule(localctx, 18, self.RULE_damage_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(DNDParser.T__11)
            self.state = 74
            self.match(DNDParser.SEP)
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DNDParser.NUM_INT]:
                self.state = 75
                self.match(DNDParser.NUM_INT)
                self.state = 76
                self.match(DNDParser.DICE)
                pass
            elif token in [DNDParser.IDENT]:
                self.state = 77
                self.match(DNDParser.IDENT)
                self.state = 78
                self.match(DNDParser.DICE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





