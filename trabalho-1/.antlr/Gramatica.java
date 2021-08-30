// Generated from /home/renan/bcc/compiladores/compiladores/trabalho-1/Gramatica.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class Gramatica extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PALAVRA_CHAVE=1, TIPO=2, CADEIA=3, CAD_ABERTA=4, COMENTARIO=5, COMENT_ABERTO=6, 
		WS=7, NUMINT=8, NUMREAL=9, OP=10, OP_LOGIC=11, IDENT=12, SIMBOLO=13, ESCOPO=14;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PALAVRA_CHAVE", "TIPO", "CADEIA", "CAD_ABERTA", "ESC_SEQ", "COMENTARIO", 
			"COMENT_ABERTO", "WS", "NUMINT", "NUMREAL", "OP", "OP_LOGIC", "IDENT", 
			"SIMBOLO", "ESCOPO"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PALAVRA_CHAVE", "TIPO", "CADEIA", "CAD_ABERTA", "COMENTARIO", 
			"COMENT_ABERTO", "WS", "NUMINT", "NUMREAL", "OP", "OP_LOGIC", "IDENT", 
			"SIMBOLO", "ESCOPO"
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


	public Gramatica(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Gramatica.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20\u0177\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\5\2\u00c8\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00e2\n"+
		"\3\3\4\3\4\3\4\7\4\u00e7\n\4\f\4\16\4\u00ea\13\4\3\4\3\4\3\5\3\5\7\5\u00f0"+
		"\n\5\f\5\16\5\u00f3\13\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\7\7\u00fc\n\7\f\7"+
		"\16\7\u00ff\13\7\3\7\5\7\u0102\n\7\3\7\3\7\3\7\3\7\3\b\3\b\7\b\u010a\n"+
		"\b\f\b\16\b\u010d\13\b\3\t\3\t\3\t\3\t\3\n\6\n\u0114\n\n\r\n\16\n\u0115"+
		"\3\13\6\13\u0119\n\13\r\13\16\13\u011a\3\13\3\13\6\13\u011f\n\13\r\13"+
		"\16\13\u0120\5\13\u0123\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u012d"+
		"\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u016b\n\r\3\16\3\16\7\16\u016f"+
		"\n\16\f\16\16\16\u0172\13\16\3\17\3\17\3\20\3\20\2\2\21\3\3\5\4\7\5\t"+
		"\6\13\2\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33\16\35\17\37\20\3\2\r\4\2"+
		"$$^^\3\2$$\4\2\f\f\17\17\3\2\177\177\5\2\13\f\17\17\"\"\5\2,-//\61\61"+
		"\4\2\'(``\4\2C\\c|\6\2\62;C\\aac|\5\2..\60\60<<\5\2*+]]__\2\u01a9\2\3"+
		"\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2"+
		"\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33"+
		"\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3\u00c7\3\2\2\2\5\u00e1\3\2\2\2\7\u00e3"+
		"\3\2\2\2\t\u00ed\3\2\2\2\13\u00f6\3\2\2\2\r\u00f9\3\2\2\2\17\u0107\3\2"+
		"\2\2\21\u010e\3\2\2\2\23\u0113\3\2\2\2\25\u0118\3\2\2\2\27\u012c\3\2\2"+
		"\2\31\u016a\3\2\2\2\33\u016c\3\2\2\2\35\u0173\3\2\2\2\37\u0175\3\2\2\2"+
		"!\"\7g\2\2\"#\7u\2\2#$\7e\2\2$%\7t\2\2%&\7g\2\2&\'\7x\2\2\'\u00c8\7c\2"+
		"\2()\7n\2\2)*\7g\2\2*+\7k\2\2+\u00c8\7c\2\2,-\7h\2\2-.\7k\2\2./\7o\2\2"+
		"/\60\7a\2\2\60\61\7c\2\2\61\62\7n\2\2\62\63\7i\2\2\63\64\7q\2\2\64\65"+
		"\7t\2\2\65\66\7k\2\2\66\67\7v\2\2\678\7o\2\28\u00c8\7q\2\29:\7c\2\2:;"+
		"\7n\2\2;<\7i\2\2<=\7q\2\2=>\7t\2\2>?\7k\2\2?@\7v\2\2@A\7o\2\2A\u00c8\7"+
		"q\2\2BC\7f\2\2CD\7g\2\2DE\7e\2\2EF\7n\2\2FG\7c\2\2GH\7t\2\2H\u00c8\7g"+
		"\2\2IJ\7r\2\2JK\7c\2\2KL\7t\2\2L\u00c8\7c\2\2MN\7c\2\2NO\7v\2\2O\u00c8"+
		"\7g\2\2PQ\7h\2\2QR\7c\2\2RS\7e\2\2S\u00c8\7c\2\2TU\7h\2\2UV\7k\2\2VW\7"+
		"o\2\2WX\7a\2\2XY\7r\2\2YZ\7c\2\2Z[\7t\2\2[\u00c8\7c\2\2\\]\7g\2\2]^\7"+
		"p\2\2^_\7s\2\2_`\7w\2\2`a\7c\2\2ab\7p\2\2bc\7v\2\2c\u00c8\7q\2\2de\7h"+
		"\2\2ef\7k\2\2fg\7o\2\2gh\7a\2\2hi\7g\2\2ij\7p\2\2jk\7s\2\2kl\7w\2\2lm"+
		"\7c\2\2mn\7p\2\2no\7v\2\2o\u00c8\7q\2\2pq\7t\2\2qr\7g\2\2rs\7i\2\2st\7"+
		"k\2\2tu\7u\2\2uv\7v\2\2vw\7t\2\2w\u00c8\7q\2\2xy\7h\2\2yz\7k\2\2z{\7o"+
		"\2\2{|\7a\2\2|}\7t\2\2}~\7g\2\2~\177\7i\2\2\177\u0080\7k\2\2\u0080\u0081"+
		"\7u\2\2\u0081\u0082\7v\2\2\u0082\u0083\7t\2\2\u0083\u00c8\7q\2\2\u0084"+
		"\u0085\7r\2\2\u0085\u0086\7t\2\2\u0086\u0087\7q\2\2\u0087\u0088\7e\2\2"+
		"\u0088\u0089\7g\2\2\u0089\u008a\7f\2\2\u008a\u008b\7k\2\2\u008b\u008c"+
		"\7o\2\2\u008c\u008d\7g\2\2\u008d\u008e\7p\2\2\u008e\u008f\7v\2\2\u008f"+
		"\u00c8\7q\2\2\u0090\u0091\7x\2\2\u0091\u0092\7c\2\2\u0092\u00c8\7t\2\2"+
		"\u0093\u0094\7h\2\2\u0094\u0095\7k\2\2\u0095\u0096\7o\2\2\u0096\u0097"+
		"\7a\2\2\u0097\u0098\7r\2\2\u0098\u0099\7t\2\2\u0099\u009a\7q\2\2\u009a"+
		"\u009b\7e\2\2\u009b\u009c\7g\2\2\u009c\u009d\7f\2\2\u009d\u009e\7k\2\2"+
		"\u009e\u009f\7o\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2"+
		"\7v\2\2\u00a2\u00c8\7q\2\2\u00a3\u00a4\7h\2\2\u00a4\u00a5\7w\2\2\u00a5"+
		"\u00a6\7p\2\2\u00a6\u00a7\7e\2\2\u00a7\u00a8\7c\2\2\u00a8\u00c8\7q\2\2"+
		"\u00a9\u00aa\7h\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7o\2\2\u00ac\u00ad"+
		"\7a\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af\7w\2\2\u00af\u00b0\7p\2\2\u00b0"+
		"\u00b1\7e\2\2\u00b1\u00b2\7c\2\2\u00b2\u00c8\7q\2\2\u00b3\u00b4\7v\2\2"+
		"\u00b4\u00b5\7k\2\2\u00b5\u00b6\7r\2\2\u00b6\u00c8\7q\2\2\u00b7\u00b8"+
		"\7t\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7v\2\2\u00ba\u00bb\7q\2\2\u00bb"+
		"\u00bc\7t\2\2\u00bc\u00bd\7p\2\2\u00bd\u00c8\7g\2\2\u00be\u00bf\7e\2\2"+
		"\u00bf\u00c0\7q\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7u\2\2\u00c2\u00c3"+
		"\7v\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7v\2\2\u00c6"+
		"\u00c8\7g\2\2\u00c7!\3\2\2\2\u00c7(\3\2\2\2\u00c7,\3\2\2\2\u00c79\3\2"+
		"\2\2\u00c7B\3\2\2\2\u00c7I\3\2\2\2\u00c7M\3\2\2\2\u00c7P\3\2\2\2\u00c7"+
		"T\3\2\2\2\u00c7\\\3\2\2\2\u00c7d\3\2\2\2\u00c7p\3\2\2\2\u00c7x\3\2\2\2"+
		"\u00c7\u0084\3\2\2\2\u00c7\u0090\3\2\2\2\u00c7\u0093\3\2\2\2\u00c7\u00a3"+
		"\3\2\2\2\u00c7\u00a9\3\2\2\2\u00c7\u00b3\3\2\2\2\u00c7\u00b7\3\2\2\2\u00c7"+
		"\u00be\3\2\2\2\u00c8\4\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7p\2\2\u00cb"+
		"\u00cc\7v\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7t\2\2"+
		"\u00cf\u00e2\7q\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3"+
		"\7v\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6\7c\2\2\u00d6"+
		"\u00e2\7n\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7c\2\2"+
		"\u00da\u00e2\7n\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de"+
		"\7i\2\2\u00de\u00df\7k\2\2\u00df\u00e0\7e\2\2\u00e0\u00e2\7q\2\2\u00e1"+
		"\u00c9\3\2\2\2\u00e1\u00d0\3\2\2\2\u00e1\u00d7\3\2\2\2\u00e1\u00db\3\2"+
		"\2\2\u00e2\6\3\2\2\2\u00e3\u00e8\7$\2\2\u00e4\u00e7\5\13\6\2\u00e5\u00e7"+
		"\n\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8"+
		"\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00e8\3\2"+
		"\2\2\u00eb\u00ec\7$\2\2\u00ec\b\3\2\2\2\u00ed\u00f1\7$\2\2\u00ee\u00f0"+
		"\n\3\2\2\u00ef\u00ee\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1"+
		"\u00f2\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5\t\4"+
		"\2\2\u00f5\n\3\2\2\2\u00f6\u00f7\7^\2\2\u00f7\u00f8\7)\2\2\u00f8\f\3\2"+
		"\2\2\u00f9\u00fd\7}\2\2\u00fa\u00fc\n\4\2\2\u00fb\u00fa\3\2\2\2\u00fc"+
		"\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0101\3\2"+
		"\2\2\u00ff\u00fd\3\2\2\2\u0100\u0102\7\17\2\2\u0101\u0100\3\2\2\2\u0101"+
		"\u0102\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\7\177\2\2\u0104\u0105\3"+
		"\2\2\2\u0105\u0106\b\7\2\2\u0106\16\3\2\2\2\u0107\u010b\7}\2\2\u0108\u010a"+
		"\n\5\2\2\u0109\u0108\3\2\2\2\u010a\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b"+
		"\u010c\3\2\2\2\u010c\20\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u010f\t\6\2"+
		"\2\u010f\u0110\3\2\2\2\u0110\u0111\b\t\2\2\u0111\22\3\2\2\2\u0112\u0114"+
		"\4\62;\2\u0113\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0113\3\2\2\2\u0115"+
		"\u0116\3\2\2\2\u0116\24\3\2\2\2\u0117\u0119\4\62;\2\u0118\u0117\3\2\2"+
		"\2\u0119\u011a\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u0122"+
		"\3\2\2\2\u011c\u011e\7\60\2\2\u011d\u011f\4\62;\2\u011e\u011d\3\2\2\2"+
		"\u011f\u0120\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123"+
		"\3\2\2\2\u0122\u011c\3\2\2\2\u0122\u0123\3\2\2\2\u0123\26\3\2\2\2\u0124"+
		"\u012d\t\7\2\2\u0125\u0126\7>\2\2\u0126\u012d\7/\2\2\u0127\u0128\7\60"+
		"\2\2\u0128\u012d\7\60\2\2\u0129\u012a\7>\2\2\u012a\u012d\7@\2\2\u012b"+
		"\u012d\t\b\2\2\u012c\u0124\3\2\2\2\u012c\u0125\3\2\2\2\u012c\u0127\3\2"+
		"\2\2\u012c\u0129\3\2\2\2\u012c\u012b\3\2\2\2\u012d\30\3\2\2\2\u012e\u016b"+
		"\7g\2\2\u012f\u0130\7q\2\2\u0130\u016b\7w\2\2\u0131\u0132\7p\2\2\u0132"+
		"\u0133\7c\2\2\u0133\u016b\7q\2\2\u0134\u016b\4>@\2\u0135\u0136\7>\2\2"+
		"\u0136\u016b\7?\2\2\u0137\u0138\7@\2\2\u0138\u016b\7?\2\2\u0139\u013a"+
		"\7u\2\2\u013a\u016b\7g\2\2\u013b\u013c\7u\2\2\u013c\u013d\7g\2\2\u013d"+
		"\u013e\7p\2\2\u013e\u013f\7c\2\2\u013f\u016b\7q\2\2\u0140\u0141\7h\2\2"+
		"\u0141\u0142\7k\2\2\u0142\u0143\7o\2\2\u0143\u0144\7a\2\2\u0144\u0145"+
		"\7u\2\2\u0145\u016b\7g\2\2\u0146\u0147\7g\2\2\u0147\u0148\7p\2\2\u0148"+
		"\u0149\7v\2\2\u0149\u014a\7c\2\2\u014a\u016b\7q\2\2\u014b\u014c\7e\2\2"+
		"\u014c\u014d\7c\2\2\u014d\u014e\7u\2\2\u014e\u016b\7q\2\2\u014f\u0150"+
		"\7u\2\2\u0150\u0151\7g\2\2\u0151\u0152\7l\2\2\u0152\u016b\7c\2\2\u0153"+
		"\u0154\7h\2\2\u0154\u0155\7k\2\2\u0155\u0156\7o\2\2\u0156\u0157\7a\2\2"+
		"\u0157\u0158\7e\2\2\u0158\u0159\7c\2\2\u0159\u015a\7u\2\2\u015a\u016b"+
		"\7q\2\2\u015b\u015c\7h\2\2\u015c\u015d\7c\2\2\u015d\u015e\7n\2\2\u015e"+
		"\u015f\7u\2\2\u015f\u016b\7q\2\2\u0160\u0161\7x\2\2\u0161\u0162\7g\2\2"+
		"\u0162\u0163\7t\2\2\u0163\u0164\7f\2\2\u0164\u0165\7c\2\2\u0165\u0166"+
		"\7f\2\2\u0166\u0167\7g\2\2\u0167\u0168\7k\2\2\u0168\u0169\7t\2\2\u0169"+
		"\u016b\7q\2\2\u016a\u012e\3\2\2\2\u016a\u012f\3\2\2\2\u016a\u0131\3\2"+
		"\2\2\u016a\u0134\3\2\2\2\u016a\u0135\3\2\2\2\u016a\u0137\3\2\2\2\u016a"+
		"\u0139\3\2\2\2\u016a\u013b\3\2\2\2\u016a\u0140\3\2\2\2\u016a\u0146\3\2"+
		"\2\2\u016a\u014b\3\2\2\2\u016a\u014f\3\2\2\2\u016a\u0153\3\2\2\2\u016a"+
		"\u015b\3\2\2\2\u016a\u0160\3\2\2\2\u016b\32\3\2\2\2\u016c\u0170\t\t\2"+
		"\2\u016d\u016f\t\n\2\2\u016e\u016d\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e"+
		"\3\2\2\2\u0170\u0171\3\2\2\2\u0171\34\3\2\2\2\u0172\u0170\3\2\2\2\u0173"+
		"\u0174\t\13\2\2\u0174\36\3\2\2\2\u0175\u0176\t\f\2\2\u0176 \3\2\2\2\22"+
		"\2\u00c7\u00e1\u00e6\u00e8\u00f1\u00fd\u0101\u010b\u0115\u011a\u0120\u0122"+
		"\u012c\u016a\u0170\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}