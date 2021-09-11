// Generated from /home/renan/bcc/compiladores/compiladores/trabalho-2/G.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class G extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROGRAMA=1, DECLARACOES=2, DECL_LOCAL_GLOBAL=3, DECLARACAO_LOCAL=4, VARIAVEL=5, 
		IDENTIFICADOR=6, DIMENSAO=7, TIPO=8, TIPO_BASICO=9, TIPO_BASICO_IDENT=10, 
		TIPO_ESTENDIDO=11, VALOR_CONSTANTE=12, REGISTRO=13, DECLARACAO_GLOBAL=14, 
		PARAMETRO=15, PARAMETROS=16, CORPO=17, CMD=18, CMDLEIA=19, CMDESCREVA=20, 
		CMDSE=21, CMDCASO=22, CMDPARA=23, CMDENQUANTO=24, CMDFACA=25, CMDATRIBUICAO=26, 
		CMDCHAMADA=27, CMDRETORNE=28, SELECAO=29, ITEM_SELECAO=30, CONSTANTES=31, 
		NUMERO_INTERVALO=32, OP_UNARIO=33, EXP_ARITMETICA=34, TERMO=35, FATOR=36, 
		OP1=37, OP2=38, OP3=39, PARCELA=40, PARCELA_UNARIO=41, PARCELA_NAO_UNARIO=42, 
		EXP_RELACIONAL=43, OP_RELACIONAL=44, EXPRESSAO=45, TERMO_LOGICO=46, FATOR_LOGICO=47, 
		PARCELA_logica=48, OP_LOGICO_1=49, OP_LOGICO_2=50, IDENT=51, NUM_INT=52, 
		NUM_REAL=53, CADEIA=54, CAD_ABERTA=55, COMENTARIO=56, COMENT_ABERTO=57, 
		WS=58;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PROGRAMA", "DECLARACOES", "DECL_LOCAL_GLOBAL", "DECLARACAO_LOCAL", "VARIAVEL", 
			"IDENTIFICADOR", "DIMENSAO", "TIPO", "TIPO_BASICO", "TIPO_BASICO_IDENT", 
			"TIPO_ESTENDIDO", "VALOR_CONSTANTE", "REGISTRO", "DECLARACAO_GLOBAL", 
			"PARAMETRO", "PARAMETROS", "CORPO", "CMD", "CMDLEIA", "CMDESCREVA", "CMDSE", 
			"CMDCASO", "CMDPARA", "CMDENQUANTO", "CMDFACA", "CMDATRIBUICAO", "CMDCHAMADA", 
			"CMDRETORNE", "SELECAO", "ITEM_SELECAO", "CONSTANTES", "NUMERO_INTERVALO", 
			"OP_UNARIO", "EXP_ARITMETICA", "TERMO", "FATOR", "OP1", "OP2", "OP3", 
			"PARCELA", "PARCELA_UNARIO", "PARCELA_NAO_UNARIO", "EXP_RELACIONAL", 
			"OP_RELACIONAL", "EXPRESSAO", "TERMO_LOGICO", "FATOR_LOGICO", "PARCELA_logica", 
			"OP_LOGICO_1", "OP_LOGICO_2", "IDENT", "NUM_INT", "NUM_REAL", "CADEIA", 
			"CAD_ABERTA", "ESC_SEQ", "COMENTARIO", "COMENT_ABERTO", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, "'-'", null, null, 
			null, null, null, "'%'", null, null, null, null, null, null, null, null, 
			null, "'ou'", "'e'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAMA", "DECLARACOES", "DECL_LOCAL_GLOBAL", "DECLARACAO_LOCAL", 
			"VARIAVEL", "IDENTIFICADOR", "DIMENSAO", "TIPO", "TIPO_BASICO", "TIPO_BASICO_IDENT", 
			"TIPO_ESTENDIDO", "VALOR_CONSTANTE", "REGISTRO", "DECLARACAO_GLOBAL", 
			"PARAMETRO", "PARAMETROS", "CORPO", "CMD", "CMDLEIA", "CMDESCREVA", "CMDSE", 
			"CMDCASO", "CMDPARA", "CMDENQUANTO", "CMDFACA", "CMDATRIBUICAO", "CMDCHAMADA", 
			"CMDRETORNE", "SELECAO", "ITEM_SELECAO", "CONSTANTES", "NUMERO_INTERVALO", 
			"OP_UNARIO", "EXP_ARITMETICA", "TERMO", "FATOR", "OP1", "OP2", "OP3", 
			"PARCELA", "PARCELA_UNARIO", "PARCELA_NAO_UNARIO", "EXP_RELACIONAL", 
			"OP_RELACIONAL", "EXPRESSAO", "TERMO_LOGICO", "FATOR_LOGICO", "PARCELA_logica", 
			"OP_LOGICO_1", "OP_LOGICO_2", "IDENT", "NUM_INT", "NUM_REAL", "CADEIA", 
			"CAD_ABERTA", "COMENTARIO", "COMENT_ABERTO", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public G(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "G.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<\u038f\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\7\3\u0095\n\3\f\3\16\3\u0098\13\3\3\4"+
		"\3\4\5\4\u009c\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\5\5\u00c0\n\5\3\6\3\6\3\6\7\6\u00c5\n\6\f\6\16\6\u00c8"+
		"\13\6\3\6\3\6\3\6\3\7\3\7\3\7\7\7\u00d0\n\7\f\7\16\7\u00d3\13\7\3\7\3"+
		"\7\3\b\3\b\3\b\3\b\7\b\u00db\n\b\f\b\16\b\u00de\13\b\3\t\3\t\5\t\u00e2"+
		"\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00fc\n\n\3\13\3\13\5\13\u0100\n\13"+
		"\3\f\5\f\u0103\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0119\n\r\3\16\3\16\3\16\3\16\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\7\16\u0125\n\16\f\16\16\16\u0128\13\16\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5"+
		"\17\u0147\n\17\3\17\3\17\7\17\u014b\n\17\f\17\16\17\u014e\13\17\3\17\7"+
		"\17\u0151\n\17\f\17\16\17\u0154\13\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0171\n\17\3\17\3\17\3\17\3\17"+
		"\7\17\u0177\n\17\f\17\16\17\u017a\13\17\3\17\7\17\u017d\n\17\f\17\16\17"+
		"\u0180\13\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5"+
		"\17\u018d\n\17\3\20\3\20\3\20\5\20\u0192\n\20\3\20\3\20\3\20\7\20\u0197"+
		"\n\20\f\20\16\20\u019a\13\20\3\20\3\20\3\20\3\21\3\21\3\21\7\21\u01a2"+
		"\n\21\f\21\16\21\u01a5\13\21\3\22\7\22\u01a8\n\22\f\22\16\22\u01ab\13"+
		"\22\3\22\7\22\u01ae\n\22\f\22\16\22\u01b1\13\22\3\23\3\23\3\23\3\23\3"+
		"\23\3\23\3\23\3\23\3\23\3\23\5\23\u01bd\n\23\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\5\24\u01c6\n\24\3\24\3\24\3\24\5\24\u01cb\n\24\3\24\7\24\u01ce"+
		"\n\24\f\24\16\24\u01d1\13\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3"+
		"\25\3\25\3\25\3\25\3\25\3\25\7\25\u01e1\n\25\f\25\16\25\u01e4\13\25\3"+
		"\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u01f3"+
		"\n\26\f\26\16\26\u01f6\13\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u01ff"+
		"\n\26\f\26\16\26\u0202\13\26\5\26\u0204\n\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0220\n\27\f\27\16\27\u0223\13"+
		"\27\5\27\u0225\n\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0245\n\30\f\30\16\30\u0248\13\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0263\n\31"+
		"\f\31\16\31\u0266\13\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3"+
		"\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u027b\n\32\f\32"+
		"\16\32\u027e\13\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\5\33\u0287\n\33"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\7\34\u0294\n\34"+
		"\f\34\16\34\u0297\13\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3"+
		"\35\3\35\3\35\3\36\7\36\u02a6\n\36\f\36\16\36\u02a9\13\36\3\37\3\37\3"+
		"\37\7\37\u02ae\n\37\f\37\16\37\u02b1\13\37\3 \3 \3 \7 \u02b6\n \f \16"+
		" \u02b9\13 \3!\5!\u02bc\n!\3!\3!\3!\3!\3!\5!\u02c3\n!\3!\5!\u02c6\n!\3"+
		"\"\3\"\3#\3#\3#\3#\7#\u02ce\n#\f#\16#\u02d1\13#\3$\3$\3$\3$\7$\u02d7\n"+
		"$\f$\16$\u02da\13$\3%\3%\3%\3%\7%\u02e0\n%\f%\16%\u02e3\13%\3&\3&\3\'"+
		"\3\'\3(\3(\3)\5)\u02ec\n)\3)\3)\5)\u02f0\n)\3*\5*\u02f3\n*\3*\3*\3*\3"+
		"*\3*\3*\7*\u02fb\n*\f*\16*\u02fe\13*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u0308"+
		"\n*\3+\3+\3+\5+\u030d\n+\3,\3,\3,\3,\5,\u0313\n,\3-\3-\3-\3-\3-\3-\3-"+
		"\3-\5-\u031d\n-\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\5\60\u032a\n\60"+
		"\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61"+
		"\3\61\3\61\3\61\5\61\u033d\n\61\3\61\5\61\u0340\n\61\3\62\3\62\3\62\3"+
		"\63\3\63\3\64\3\64\7\64\u0349\n\64\f\64\16\64\u034c\13\64\3\65\6\65\u034f"+
		"\n\65\r\65\16\65\u0350\3\66\6\66\u0354\n\66\r\66\16\66\u0355\3\66\3\66"+
		"\6\66\u035a\n\66\r\66\16\66\u035b\5\66\u035e\n\66\3\67\3\67\3\67\7\67"+
		"\u0363\n\67\f\67\16\67\u0366\13\67\3\67\3\67\38\38\78\u036c\n8\f8\168"+
		"\u036f\138\38\58\u0372\n8\39\39\39\3:\3:\7:\u0379\n:\f:\16:\u037c\13:"+
		"\3:\5:\u037f\n:\3:\3:\3:\3:\3;\3;\7;\u0387\n;\f;\16;\u038a\13;\3<\3<\3"+
		"<\3<\2\2=\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33"+
		"\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67"+
		"\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65"+
		"i\66k\67m8o9q\2s:u;w<\3\2\r\4\2--//\4\2,,\61\61\4\2>>@@\5\2C\\aac|\6\2"+
		"\62;C\\aac|\6\2\f\f\17\17$$^^\3\2$$\4\2\f\f\17\17\5\2\f\f\17\17\177\177"+
		"\3\2\177\177\5\2\13\f\17\17\"\"\2\u03e8\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3"+
		"\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2"+
		"\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35"+
		"\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)"+
		"\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2"+
		"\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2"+
		"A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3"+
		"\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2"+
		"\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2"+
		"g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2s\3\2\2\2\2u\3"+
		"\2\2\2\2w\3\2\2\2\3y\3\2\2\2\5\u0096\3\2\2\2\7\u009b\3\2\2\2\t\u00bf\3"+
		"\2\2\2\13\u00c1\3\2\2\2\r\u00cc\3\2\2\2\17\u00dc\3\2\2\2\21\u00e1\3\2"+
		"\2\2\23\u00fb\3\2\2\2\25\u00ff\3\2\2\2\27\u0102\3\2\2\2\31\u0118\3\2\2"+
		"\2\33\u011a\3\2\2\2\35\u018c\3\2\2\2\37\u0191\3\2\2\2!\u019e\3\2\2\2#"+
		"\u01a9\3\2\2\2%\u01bc\3\2\2\2\'\u01be\3\2\2\2)\u01d4\3\2\2\2+\u01e7\3"+
		"\2\2\2-\u020c\3\2\2\2/\u022f\3\2\2\2\61\u0252\3\2\2\2\63\u0274\3\2\2\2"+
		"\65\u0286\3\2\2\2\67\u028e\3\2\2\29\u029a\3\2\2\2;\u02a7\3\2\2\2=\u02aa"+
		"\3\2\2\2?\u02b2\3\2\2\2A\u02bb\3\2\2\2C\u02c7\3\2\2\2E\u02c9\3\2\2\2G"+
		"\u02d2\3\2\2\2I\u02db\3\2\2\2K\u02e4\3\2\2\2M\u02e6\3\2\2\2O\u02e8\3\2"+
		"\2\2Q\u02ef\3\2\2\2S\u0307\3\2\2\2U\u030c\3\2\2\2W\u030e\3\2\2\2Y\u031c"+
		"\3\2\2\2[\u031e\3\2\2\2]\u0322\3\2\2\2_\u0329\3\2\2\2a\u033f\3\2\2\2c"+
		"\u0341\3\2\2\2e\u0344\3\2\2\2g\u0346\3\2\2\2i\u034e\3\2\2\2k\u0353\3\2"+
		"\2\2m\u035f\3\2\2\2o\u0369\3\2\2\2q\u0373\3\2\2\2s\u0376\3\2\2\2u\u0384"+
		"\3\2\2\2w\u038b\3\2\2\2yz\5\5\3\2z{\7c\2\2{|\7n\2\2|}\7i\2\2}~\7q\2\2"+
		"~\177\7t\2\2\177\u0080\7k\2\2\u0080\u0081\7v\2\2\u0081\u0082\7o\2\2\u0082"+
		"\u0083\7q\2\2\u0083\u0084\3\2\2\2\u0084\u0085\5#\22\2\u0085\u0086\7h\2"+
		"\2\u0086\u0087\7k\2\2\u0087\u0088\7o\2\2\u0088\u0089\7a\2\2\u0089\u008a"+
		"\7c\2\2\u008a\u008b\7n\2\2\u008b\u008c\7i\2\2\u008c\u008d\7q\2\2\u008d"+
		"\u008e\7t\2\2\u008e\u008f\7k\2\2\u008f\u0090\7v\2\2\u0090\u0091\7o\2\2"+
		"\u0091\u0092\7q\2\2\u0092\4\3\2\2\2\u0093\u0095\5\7\4\2\u0094\u0093\3"+
		"\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097"+
		"\6\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009c\5\t\5\2\u009a\u009c\5\35\17"+
		"\2\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c\b\3\2\2\2\u009d\u009e"+
		"\7f\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7e\2\2\u00a0\u00a1\7n\2\2\u00a1"+
		"\u00a2\7c\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5\3\2\2"+
		"\2\u00a5\u00c0\5\13\6\2\u00a6\u00a7\7e\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9"+
		"\7p\2\2\u00a9\u00aa\7u\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7c\2\2\u00ac"+
		"\u00ad\7p\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\3\2\2"+
		"\2\u00b0\u00b1\5g\64\2\u00b1\u00b2\7<\2\2\u00b2\u00b3\5\23\n\2\u00b3\u00b4"+
		"\7?\2\2\u00b4\u00b5\5\31\r\2\u00b5\u00c0\3\2\2\2\u00b6\u00b7\7V\2\2\u00b7"+
		"\u00b8\7K\2\2\u00b8\u00b9\7R\2\2\u00b9\u00ba\7Q\2\2\u00ba\u00bb\3\2\2"+
		"\2\u00bb\u00bc\5g\64\2\u00bc\u00bd\7<\2\2\u00bd\u00be\5\21\t\2\u00be\u00c0"+
		"\3\2\2\2\u00bf\u009d\3\2\2\2\u00bf\u00a6\3\2\2\2\u00bf\u00b6\3\2\2\2\u00c0"+
		"\n\3\2\2\2\u00c1\u00c6\5\r\7\2\u00c2\u00c3\7.\2\2\u00c3\u00c5\5\r\7\2"+
		"\u00c4\u00c2\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7"+
		"\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\7<\2\2\u00ca"+
		"\u00cb\5\21\t\2\u00cb\f\3\2\2\2\u00cc\u00d1\5g\64\2\u00cd\u00ce\7\60\2"+
		"\2\u00ce\u00d0\5g\64\2\u00cf\u00cd\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf"+
		"\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4"+
		"\u00d5\5\17\b\2\u00d5\16\3\2\2\2\u00d6\u00d7\7]\2\2\u00d7\u00d8\5E#\2"+
		"\u00d8\u00d9\7_\2\2\u00d9\u00db\3\2\2\2\u00da\u00d6\3\2\2\2\u00db\u00de"+
		"\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\20\3\2\2\2\u00de"+
		"\u00dc\3\2\2\2\u00df\u00e2\5\33\16\2\u00e0\u00e2\5\27\f\2\u00e1\u00df"+
		"\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2\22\3\2\2\2\u00e3\u00e4\7n\2\2\u00e4"+
		"\u00e5\7k\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8\7t\2\2"+
		"\u00e8\u00e9\7c\2\2\u00e9\u00fc\7n\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec"+
		"\7p\2\2\u00ec\u00ed\7v\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7k\2\2\u00ef"+
		"\u00f0\7t\2\2\u00f0\u00fc\7q\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3\7g\2\2"+
		"\u00f3\u00f4\7c\2\2\u00f4\u00fc\7n\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7"+
		"\7q\2\2\u00f7\u00f8\7i\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7e\2\2\u00fa"+
		"\u00fc\7q\2\2\u00fb\u00e3\3\2\2\2\u00fb\u00ea\3\2\2\2\u00fb\u00f1\3\2"+
		"\2\2\u00fb\u00f5\3\2\2\2\u00fc\24\3\2\2\2\u00fd\u0100\5\23\n\2\u00fe\u0100"+
		"\5g\64\2\u00ff\u00fd\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100\26\3\2\2\2\u0101"+
		"\u0103\7`\2\2\u0102\u0101\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\3\2"+
		"\2\2\u0104\u0105\5\25\13\2\u0105\30\3\2\2\2\u0106\u0119\5m\67\2\u0107"+
		"\u0119\5i\65\2\u0108\u0119\5k\66\2\u0109\u010a\7x\2\2\u010a\u010b\7g\2"+
		"\2\u010b\u010c\7t\2\2\u010c\u010d\7f\2\2\u010d\u010e\7c\2\2\u010e\u010f"+
		"\7f\2\2\u010f\u0110\7g\2\2\u0110\u0111\7k\2\2\u0111\u0112\7t\2\2\u0112"+
		"\u0119\7q\2\2\u0113\u0114\7h\2\2\u0114\u0115\7c\2\2\u0115\u0116\7n\2\2"+
		"\u0116\u0117\7u\2\2\u0117\u0119\7q\2\2\u0118\u0106\3\2\2\2\u0118\u0107"+
		"\3\2\2\2\u0118\u0108\3\2\2\2\u0118\u0109\3\2\2\2\u0118\u0113\3\2\2\2\u0119"+
		"\32\3\2\2\2\u011a\u011b\7T\2\2\u011b\u011c\7G\2\2\u011c\u011d\7I\2\2\u011d"+
		"\u011e\7K\2\2\u011e\u011f\7U\2\2\u011f\u0120\7V\2\2\u0120\u0121\7T\2\2"+
		"\u0121\u0122\7Q\2\2\u0122\u0126\3\2\2\2\u0123\u0125\5\13\6\2\u0124\u0123"+
		"\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127"+
		"\u0129\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012a\7h\2\2\u012a\u012b\7k\2"+
		"\2\u012b\u012c\7o\2\2\u012c\u012d\7a\2\2\u012d\u012e\7T\2\2\u012e\u012f"+
		"\7G\2\2\u012f\u0130\7I\2\2\u0130\u0131\7K\2\2\u0131\u0132\7U\2\2\u0132"+
		"\u0133\7V\2\2\u0133\u0134\7T\2\2\u0134\u0135\7Q\2\2\u0135\34\3\2\2\2\u0136"+
		"\u0137\7r\2\2\u0137\u0138\7t\2\2\u0138\u0139\7q\2\2\u0139\u013a\7e\2\2"+
		"\u013a\u013b\7g\2\2\u013b\u013c\7f\2\2\u013c\u013d\7k\2\2\u013d\u013e"+
		"\7o\2\2\u013e\u013f\7g\2\2\u013f\u0140\7p\2\2\u0140\u0141\7v\2\2\u0141"+
		"\u0142\7q\2\2\u0142\u0143\3\2\2\2\u0143\u0144\5g\64\2\u0144\u0146\7*\2"+
		"\2\u0145\u0147\5!\21\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148"+
		"\3\2\2\2\u0148\u014c\7+\2\2\u0149\u014b\5\t\5\2\u014a\u0149\3\2\2\2\u014b"+
		"\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u0152\3\2"+
		"\2\2\u014e\u014c\3\2\2\2\u014f\u0151\5%\23\2\u0150\u014f\3\2\2\2\u0151"+
		"\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0155\3\2"+
		"\2\2\u0154\u0152\3\2\2\2\u0155\u0156\7h\2\2\u0156\u0157\7k\2\2\u0157\u0158"+
		"\7o\2\2\u0158\u0159\7a\2\2\u0159\u015a\7r\2\2\u015a\u015b\7t\2\2\u015b"+
		"\u015c\7q\2\2\u015c\u015d\7e\2\2\u015d\u015e\7g\2\2\u015e\u015f\7f\2\2"+
		"\u015f\u0160\7k\2\2\u0160\u0161\7o\2\2\u0161\u0162\7g\2\2\u0162\u0163"+
		"\7p\2\2\u0163\u0164\7v\2\2\u0164\u0165\7q\2\2\u0165\u018d\3\2\2\2\u0166"+
		"\u0167\7h\2\2\u0167\u0168\7w\2\2\u0168\u0169\7p\2\2\u0169\u016a\7e\2\2"+
		"\u016a\u016b\7c\2\2\u016b\u016c\7q\2\2\u016c\u016d\3\2\2\2\u016d\u016e"+
		"\5g\64\2\u016e\u0170\7*\2\2\u016f\u0171\5!\21\2\u0170\u016f\3\2\2\2\u0170"+
		"\u0171\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\7+\2\2\u0173\u0174\7<\2"+
		"\2\u0174\u0178\5\27\f\2\u0175\u0177\5\t\5\2\u0176\u0175\3\2\2\2\u0177"+
		"\u017a\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017e\3\2"+
		"\2\2\u017a\u0178\3\2\2\2\u017b\u017d\5%\23\2\u017c\u017b\3\2\2\2\u017d"+
		"\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3\2"+
		"\2\2\u0180\u017e\3\2\2\2\u0181\u0182\7h\2\2\u0182\u0183\7k\2\2\u0183\u0184"+
		"\7o\2\2\u0184\u0185\7a\2\2\u0185\u0186\7h\2\2\u0186\u0187\7w\2\2\u0187"+
		"\u0188\7p\2\2\u0188\u0189\7e\2\2\u0189\u018a\7c\2\2\u018a\u018b\7q\2\2"+
		"\u018b\u018d\3\2\2\2\u018c\u0136\3\2\2\2\u018c\u0166\3\2\2\2\u018d\36"+
		"\3\2\2\2\u018e\u018f\7x\2\2\u018f\u0190\7c\2\2\u0190\u0192\7t\2\2\u0191"+
		"\u018e\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0198\5\r"+
		"\7\2\u0194\u0195\7.\2\2\u0195\u0197\5\r\7\2\u0196\u0194\3\2\2\2\u0197"+
		"\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\3\2"+
		"\2\2\u019a\u0198\3\2\2\2\u019b\u019c\7<\2\2\u019c\u019d\5\27\f\2\u019d"+
		" \3\2\2\2\u019e\u01a3\5\37\20\2\u019f\u01a0\7.\2\2\u01a0\u01a2\5\37\20"+
		"\2\u01a1\u019f\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4"+
		"\3\2\2\2\u01a4\"\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a8\5\t\5\2\u01a7"+
		"\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2"+
		"\2\2\u01aa\u01af\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ae\5%\23\2\u01ad"+
		"\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2"+
		"\2\2\u01b0$\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01bd\5\'\24\2\u01b3\u01bd"+
		"\5)\25\2\u01b4\u01bd\5+\26\2\u01b5\u01bd\5-\27\2\u01b6\u01bd\5/\30\2\u01b7"+
		"\u01bd\5\61\31\2\u01b8\u01bd\5\63\32\2\u01b9\u01bd\5\65\33\2\u01ba\u01bd"+
		"\5\67\34\2\u01bb\u01bd\59\35\2\u01bc\u01b2\3\2\2\2\u01bc\u01b3\3\2\2\2"+
		"\u01bc\u01b4\3\2\2\2\u01bc\u01b5\3\2\2\2\u01bc\u01b6\3\2\2\2\u01bc\u01b7"+
		"\3\2\2\2\u01bc\u01b8\3\2\2\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc"+
		"\u01bb\3\2\2\2\u01bd&\3\2\2\2\u01be\u01bf\7n\2\2\u01bf\u01c0\7g\2\2\u01c0"+
		"\u01c1\7k\2\2\u01c1\u01c2\7c\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c5\7*\2"+
		"\2\u01c4\u01c6\7`\2\2\u01c5\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7"+
		"\3\2\2\2\u01c7\u01cf\5\r\7\2\u01c8\u01ca\7.\2\2\u01c9\u01cb\7`\2\2\u01ca"+
		"\u01c9\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ce\5\r"+
		"\7\2\u01cd\u01c8\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf"+
		"\u01d0\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3\7+"+
		"\2\2\u01d3(\3\2\2\2\u01d4\u01d5\7g\2\2\u01d5\u01d6\7u\2\2\u01d6\u01d7"+
		"\7e\2\2\u01d7\u01d8\7t\2\2\u01d8\u01d9\7g\2\2\u01d9\u01da\7x\2\2\u01da"+
		"\u01db\7c\2\2\u01db\u01dc\3\2\2\2\u01dc\u01dd\7*\2\2\u01dd\u01e2\5[.\2"+
		"\u01de\u01df\7.\2\2\u01df\u01e1\5[.\2\u01e0\u01de\3\2\2\2\u01e1\u01e4"+
		"\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e5\3\2\2\2\u01e4"+
		"\u01e2\3\2\2\2\u01e5\u01e6\7+\2\2\u01e6*\3\2\2\2\u01e7\u01e8\7u\2\2\u01e8"+
		"\u01e9\7g\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb\5[.\2\u01eb\u01ec\7g\2\2"+
		"\u01ec\u01ed\7p\2\2\u01ed\u01ee\7v\2\2\u01ee\u01ef\7c\2\2\u01ef\u01f0"+
		"\7q\2\2\u01f0\u01f4\3\2\2\2\u01f1\u01f3\5%\23\2\u01f2\u01f1\3\2\2\2\u01f3"+
		"\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u0203\3\2"+
		"\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f8\7u\2\2\u01f8\u01f9\7g\2\2\u01f9\u01fa"+
		"\7p\2\2\u01fa\u01fb\7c\2\2\u01fb\u01fc\7q\2\2\u01fc\u0200\3\2\2\2\u01fd"+
		"\u01ff\5%\23\2\u01fe\u01fd\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3\2"+
		"\2\2\u0200\u0201\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0203"+
		"\u01f7\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0206\7h"+
		"\2\2\u0206\u0207\7k\2\2\u0207\u0208\7o\2\2\u0208\u0209\7a\2\2\u0209\u020a"+
		"\7u\2\2\u020a\u020b\7g\2\2\u020b,\3\2\2\2\u020c\u020d\7e\2\2\u020d\u020e"+
		"\7c\2\2\u020e\u020f\7u\2\2\u020f\u0210\7q\2\2\u0210\u0211\3\2\2\2\u0211"+
		"\u0212\5E#\2\u0212\u0213\7u\2\2\u0213\u0214\7g\2\2\u0214\u0215\7l\2\2"+
		"\u0215\u0216\7c\2\2\u0216\u0217\3\2\2\2\u0217\u0224\5;\36\2\u0218\u0219"+
		"\7u\2\2\u0219\u021a\7g\2\2\u021a\u021b\7p\2\2\u021b\u021c\7c\2\2\u021c"+
		"\u021d\7q\2\2\u021d\u0221\3\2\2\2\u021e\u0220\5%\23\2\u021f\u021e\3\2"+
		"\2\2\u0220\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222"+
		"\u0225\3\2\2\2\u0223\u0221\3\2\2\2\u0224\u0218\3\2\2\2\u0224\u0225\3\2"+
		"\2\2\u0225\u0226\3\2\2\2\u0226\u0227\7h\2\2\u0227\u0228\7k\2\2\u0228\u0229"+
		"\7o\2\2\u0229\u022a\7a\2\2\u022a\u022b\7e\2\2\u022b\u022c\7c\2\2\u022c"+
		"\u022d\7u\2\2\u022d\u022e\7q\2\2\u022e.\3\2\2\2\u022f\u0230\7r\2\2\u0230"+
		"\u0231\7c\2\2\u0231\u0232\7t\2\2\u0232\u0233\7c\2\2\u0233\u0234\3\2\2"+
		"\2\u0234\u0235\5g\64\2\u0235\u0236\7>\2\2\u0236\u0237\7/\2\2\u0237\u0238"+
		"\3\2\2\2\u0238\u0239\5E#\2\u0239\u023a\7c\2\2\u023a\u023b\7v\2\2\u023b"+
		"\u023c\7g\2\2\u023c\u023d\3\2\2\2\u023d\u023e\5E#\2\u023e\u023f\7h\2\2"+
		"\u023f\u0240\7c\2\2\u0240\u0241\7e\2\2\u0241\u0242\7c\2\2\u0242\u0246"+
		"\3\2\2\2\u0243\u0245\5%\23\2\u0244\u0243\3\2\2\2\u0245\u0248\3\2\2\2\u0246"+
		"\u0244\3\2\2\2\u0246\u0247\3\2\2\2\u0247\u0249\3\2\2\2\u0248\u0246\3\2"+
		"\2\2\u0249\u024a\7h\2\2\u024a\u024b\7k\2\2\u024b\u024c\7o\2\2\u024c\u024d"+
		"\7a\2\2\u024d\u024e\7r\2\2\u024e\u024f\7c\2\2\u024f\u0250\7t\2\2\u0250"+
		"\u0251\7c\2\2\u0251\60\3\2\2\2\u0252\u0253\7g\2\2\u0253\u0254\7p\2\2\u0254"+
		"\u0255\7s\2\2\u0255\u0256\7w\2\2\u0256\u0257\7c\2\2\u0257\u0258\7p\2\2"+
		"\u0258\u0259\7v\2\2\u0259\u025a\7q\2\2\u025a\u025b\3\2\2\2\u025b\u025c"+
		"\5[.\2\u025c\u025d\7h\2\2\u025d\u025e\7c\2\2\u025e\u025f\7e\2\2\u025f"+
		"\u0260\7c\2\2\u0260\u0264\3\2\2\2\u0261\u0263\5%\23\2\u0262\u0261\3\2"+
		"\2\2\u0263\u0266\3\2\2\2\u0264\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265"+
		"\u0267\3\2\2\2\u0266\u0264\3\2\2\2\u0267\u0268\7h\2\2\u0268\u0269\7k\2"+
		"\2\u0269\u026a\7o\2\2\u026a\u026b\7a\2\2\u026b\u026c\7g\2\2\u026c\u026d"+
		"\7p\2\2\u026d\u026e\7s\2\2\u026e\u026f\7w\2\2\u026f\u0270\7c\2\2\u0270"+
		"\u0271\7p\2\2\u0271\u0272\7v\2\2\u0272\u0273\7q\2\2\u0273\62\3\2\2\2\u0274"+
		"\u0275\7h\2\2\u0275\u0276\7c\2\2\u0276\u0277\7e\2\2\u0277\u0278\7c\2\2"+
		"\u0278\u027c\3\2\2\2\u0279\u027b\5%\23\2\u027a\u0279\3\2\2\2\u027b\u027e"+
		"\3\2\2\2\u027c\u027a\3\2\2\2\u027c\u027d\3\2\2\2\u027d\u027f\3\2\2\2\u027e"+
		"\u027c\3\2\2\2\u027f\u0280\7c\2\2\u0280\u0281\7v\2\2\u0281\u0282\7g\2"+
		"\2\u0282\u0283\3\2\2\2\u0283\u0284\5[.\2\u0284\64\3\2\2\2\u0285\u0287"+
		"\7`\2\2\u0286\u0285\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0288\3\2\2\2\u0288"+
		"\u0289\5\r\7\2\u0289\u028a\7>\2\2\u028a\u028b\7/\2\2\u028b\u028c\3\2\2"+
		"\2\u028c\u028d\5[.\2\u028d\66\3\2\2\2\u028e\u028f\5g\64\2\u028f\u0290"+
		"\7*\2\2\u0290\u0295\5[.\2\u0291\u0292\7.\2\2\u0292\u0294\5[.\2\u0293\u0291"+
		"\3\2\2\2\u0294\u0297\3\2\2\2\u0295\u0293\3\2\2\2\u0295\u0296\3\2\2\2\u0296"+
		"\u0298\3\2\2\2\u0297\u0295\3\2\2\2\u0298\u0299\7+\2\2\u02998\3\2\2\2\u029a"+
		"\u029b\7t\2\2\u029b\u029c\7g\2\2\u029c\u029d\7v\2\2\u029d\u029e\7q\2\2"+
		"\u029e\u029f\7t\2\2\u029f\u02a0\7p\2\2\u02a0\u02a1\7g\2\2\u02a1\u02a2"+
		"\3\2\2\2\u02a2\u02a3\5[.\2\u02a3:\3\2\2\2\u02a4\u02a6\5=\37\2\u02a5\u02a4"+
		"\3\2\2\2\u02a6\u02a9\3\2\2\2\u02a7\u02a5\3\2\2\2\u02a7\u02a8\3\2\2\2\u02a8"+
		"<\3\2\2\2\u02a9\u02a7\3\2\2\2\u02aa\u02ab\5? \2\u02ab\u02af\7<\2\2\u02ac"+
		"\u02ae\5%\23\2\u02ad\u02ac\3\2\2\2\u02ae\u02b1\3\2\2\2\u02af\u02ad\3\2"+
		"\2\2\u02af\u02b0\3\2\2\2\u02b0>\3\2\2\2\u02b1\u02af\3\2\2\2\u02b2\u02b7"+
		"\5A!\2\u02b3\u02b4\7.\2\2\u02b4\u02b6\5A!\2\u02b5\u02b3\3\2\2\2\u02b6"+
		"\u02b9\3\2\2\2\u02b7\u02b5\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8@\3\2\2\2"+
		"\u02b9\u02b7\3\2\2\2\u02ba\u02bc\5C\"\2\u02bb\u02ba\3\2\2\2\u02bb\u02bc"+
		"\3\2\2\2\u02bc\u02bd\3\2\2\2\u02bd\u02c5\5i\65\2\u02be\u02bf\7\60\2\2"+
		"\u02bf\u02c0\7\60\2\2\u02c0\u02c2\3\2\2\2\u02c1\u02c3\5C\"\2\u02c2\u02c1"+
		"\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3\u02c4\3\2\2\2\u02c4\u02c6\5i\65\2\u02c5"+
		"\u02be\3\2\2\2\u02c5\u02c6\3\2\2\2\u02c6B\3\2\2\2\u02c7\u02c8\7/\2\2\u02c8"+
		"D\3\2\2\2\u02c9\u02cf\5G$\2\u02ca\u02cb\5K&\2\u02cb\u02cc\5G$\2\u02cc"+
		"\u02ce\3\2\2\2\u02cd\u02ca\3\2\2\2\u02ce\u02d1\3\2\2\2\u02cf\u02cd\3\2"+
		"\2\2\u02cf\u02d0\3\2\2\2\u02d0F\3\2\2\2\u02d1\u02cf\3\2\2\2\u02d2\u02d8"+
		"\5I%\2\u02d3\u02d4\5M\'\2\u02d4\u02d5\5I%\2\u02d5\u02d7\3\2\2\2\u02d6"+
		"\u02d3\3\2\2\2\u02d7\u02da\3\2\2\2\u02d8\u02d6\3\2\2\2\u02d8\u02d9\3\2"+
		"\2\2\u02d9H\3\2\2\2\u02da\u02d8\3\2\2\2\u02db\u02e1\5Q)\2\u02dc\u02dd"+
		"\5O(\2\u02dd\u02de\5Q)\2\u02de\u02e0\3\2\2\2\u02df\u02dc\3\2\2\2\u02e0"+
		"\u02e3\3\2\2\2\u02e1\u02df\3\2\2\2\u02e1\u02e2\3\2\2\2\u02e2J\3\2\2\2"+
		"\u02e3\u02e1\3\2\2\2\u02e4\u02e5\t\2\2\2\u02e5L\3\2\2\2\u02e6\u02e7\t"+
		"\3\2\2\u02e7N\3\2\2\2\u02e8\u02e9\7\'\2\2\u02e9P\3\2\2\2\u02ea\u02ec\5"+
		"C\"\2\u02eb\u02ea\3\2\2\2\u02eb\u02ec\3\2\2\2\u02ec\u02ed\3\2\2\2\u02ed"+
		"\u02f0\5S*\2\u02ee\u02f0\5U+\2\u02ef\u02eb\3\2\2\2\u02ef\u02ee\3\2\2\2"+
		"\u02f0R\3\2\2\2\u02f1\u02f3\7`\2\2\u02f2\u02f1\3\2\2\2\u02f2\u02f3\3\2"+
		"\2\2\u02f3\u02f4\3\2\2\2\u02f4\u0308\5\r\7\2\u02f5\u02f6\5g\64\2\u02f6"+
		"\u02f7\7*\2\2\u02f7\u02fc\5[.\2\u02f8\u02f9\7.\2\2\u02f9\u02fb\5[.\2\u02fa"+
		"\u02f8\3\2\2\2\u02fb\u02fe\3\2\2\2\u02fc\u02fa\3\2\2\2\u02fc\u02fd\3\2"+
		"\2\2\u02fd\u02ff\3\2\2\2\u02fe\u02fc\3\2\2\2\u02ff\u0300\7+\2\2\u0300"+
		"\u0308\3\2\2\2\u0301\u0308\5i\65\2\u0302\u0308\5k\66\2\u0303\u0304\7*"+
		"\2\2\u0304\u0305\5[.\2\u0305\u0306\7+\2\2\u0306\u0308\3\2\2\2\u0307\u02f2"+
		"\3\2\2\2\u0307\u02f5\3\2\2\2\u0307\u0301\3\2\2\2\u0307\u0302\3\2\2\2\u0307"+
		"\u0303\3\2\2\2\u0308T\3\2\2\2\u0309\u030a\7(\2\2\u030a\u030d\5\r\7\2\u030b"+
		"\u030d\5m\67\2\u030c\u0309\3\2\2\2\u030c\u030b\3\2\2\2\u030dV\3\2\2\2"+
		"\u030e\u0312\5E#\2\u030f\u0310\5Y-\2\u0310\u0311\5E#\2\u0311\u0313\3\2"+
		"\2\2\u0312\u030f\3\2\2\2\u0312\u0313\3\2\2\2\u0313X\3\2\2\2\u0314\u031d"+
		"\7?\2\2\u0315\u0316\7>\2\2\u0316\u031d\7@\2\2\u0317\u0318\7@\2\2\u0318"+
		"\u031d\7?\2\2\u0319\u031a\7>\2\2\u031a\u031d\7?\2\2\u031b\u031d\t\4\2"+
		"\2\u031c\u0314\3\2\2\2\u031c\u0315\3\2\2\2\u031c\u0317\3\2\2\2\u031c\u0319"+
		"\3\2\2\2\u031c\u031b\3\2\2\2\u031dZ\3\2\2\2\u031e\u031f\5]/\2\u031f\u0320"+
		"\5c\62\2\u0320\u0321\5]/\2\u0321\\\3\2\2\2\u0322\u0323\5_\60\2\u0323\u0324"+
		"\5e\63\2\u0324\u0325\5_\60\2\u0325^\3\2\2\2\u0326\u0327\7p\2\2\u0327\u0328"+
		"\7c\2\2\u0328\u032a\7q\2\2\u0329\u0326\3\2\2\2\u0329\u032a\3\2\2\2\u032a"+
		"\u032b\3\2\2\2\u032b\u032c\5a\61\2\u032c`\3\2\2\2\u032d\u032e\7x\2\2\u032e"+
		"\u032f\7g\2\2\u032f\u0330\7t\2\2\u0330\u0331\7f\2\2\u0331\u0332\7c\2\2"+
		"\u0332\u0333\7f\2\2\u0333\u0334\7g\2\2\u0334\u0335\7k\2\2\u0335\u0336"+
		"\7t\2\2\u0336\u033d\7q\2\2\u0337\u0338\7h\2\2\u0338\u0339\7c\2\2\u0339"+
		"\u033a\7n\2\2\u033a\u033b\7u\2\2\u033b\u033d\7q\2\2\u033c\u032d\3\2\2"+
		"\2\u033c\u0337\3\2\2\2\u033d\u0340\3\2\2\2\u033e\u0340\5W,\2\u033f\u033c"+
		"\3\2\2\2\u033f\u033e\3\2\2\2\u0340b\3\2\2\2\u0341\u0342\7q\2\2\u0342\u0343"+
		"\7w\2\2\u0343d\3\2\2\2\u0344\u0345\7g\2\2\u0345f\3\2\2\2\u0346\u034a\t"+
		"\5\2\2\u0347\u0349\t\6\2\2\u0348\u0347\3\2\2\2\u0349\u034c\3\2\2\2\u034a"+
		"\u0348\3\2\2\2\u034a\u034b\3\2\2\2\u034bh\3\2\2\2\u034c\u034a\3\2\2\2"+
		"\u034d\u034f\4\62;\2\u034e\u034d\3\2\2\2\u034f\u0350\3\2\2\2\u0350\u034e"+
		"\3\2\2\2\u0350\u0351\3\2\2\2\u0351j\3\2\2\2\u0352\u0354\4\62;\2\u0353"+
		"\u0352\3\2\2\2\u0354\u0355\3\2\2\2\u0355\u0353\3\2\2\2\u0355\u0356\3\2"+
		"\2\2\u0356\u035d\3\2\2\2\u0357\u0359\7\60\2\2\u0358\u035a\4\62;\2\u0359"+
		"\u0358\3\2\2\2\u035a\u035b\3\2\2\2\u035b\u0359\3\2\2\2\u035b\u035c\3\2"+
		"\2\2\u035c\u035e\3\2\2\2\u035d\u0357\3\2\2\2\u035d\u035e\3\2\2\2\u035e"+
		"l\3\2\2\2\u035f\u0364\7$\2\2\u0360\u0363\5q9\2\u0361\u0363\n\7\2\2\u0362"+
		"\u0360\3\2\2\2\u0362\u0361\3\2\2\2\u0363\u0366\3\2\2\2\u0364\u0362\3\2"+
		"\2\2\u0364\u0365\3\2\2\2\u0365\u0367\3\2\2\2\u0366\u0364\3\2\2\2\u0367"+
		"\u0368\7$\2\2\u0368n\3\2\2\2\u0369\u036d\7$\2\2\u036a\u036c\n\b\2\2\u036b"+
		"\u036a\3\2\2\2\u036c\u036f\3\2\2\2\u036d\u036b\3\2\2\2\u036d\u036e\3\2"+
		"\2\2\u036e\u0371\3\2\2\2\u036f\u036d\3\2\2\2\u0370\u0372\t\t\2\2\u0371"+
		"\u0370\3\2\2\2\u0371\u0372\3\2\2\2\u0372p\3\2\2\2\u0373\u0374\7^\2\2\u0374"+
		"\u0375\7)\2\2\u0375r\3\2\2\2\u0376\u037a\7}\2\2\u0377\u0379\n\n\2\2\u0378"+
		"\u0377\3\2\2\2\u0379\u037c\3\2\2\2\u037a\u0378\3\2\2\2\u037a\u037b\3\2"+
		"\2\2\u037b\u037e\3\2\2\2\u037c\u037a\3\2\2\2\u037d\u037f\7\17\2\2\u037e"+
		"\u037d\3\2\2\2\u037e\u037f\3\2\2\2\u037f\u0380\3\2\2\2\u0380\u0381\7\177"+
		"\2\2\u0381\u0382\3\2\2\2\u0382\u0383\b:\2\2\u0383t\3\2\2\2\u0384\u0388"+
		"\7}\2\2\u0385\u0387\n\13\2\2\u0386\u0385\3\2\2\2\u0387\u038a\3\2\2\2\u0388"+
		"\u0386\3\2\2\2\u0388\u0389\3\2\2\2\u0389v\3\2\2\2\u038a\u0388\3\2\2\2"+
		"\u038b\u038c\t\f\2\2\u038c\u038d\3\2\2\2\u038d\u038e\b<\2\2\u038ex\3\2"+
		"\2\2J\2\u0096\u009b\u00bf\u00c6\u00d1\u00dc\u00e1\u00fb\u00ff\u0102\u0118"+
		"\u0126\u0146\u014c\u0152\u0170\u0178\u017e\u018c\u0191\u0198\u01a3\u01a9"+
		"\u01af\u01bc\u01c5\u01ca\u01cf\u01e2\u01f4\u0200\u0203\u0221\u0224\u0246"+
		"\u0264\u027c\u0286\u0295\u02a7\u02af\u02b7\u02bb\u02c2\u02c5\u02cf\u02d8"+
		"\u02e1\u02eb\u02ef\u02f2\u02fc\u0307\u030c\u0312\u031c\u0329\u033c\u033f"+
		"\u034a\u0350\u0355\u035b\u035d\u0362\u0364\u036d\u0371\u037a\u037e\u0388"+
		"\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}