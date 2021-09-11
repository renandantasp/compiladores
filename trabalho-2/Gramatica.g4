lexer grammar Gramatica;


PROGRAMA : 
DECLARACOES 'algoritmo' CORPO 'fim_algoritmo';

DECLARACOES : 
(DECL_LOCAL_GLOBAL)*;

DECL_LOCAL_GLOBAL : 
DECLARACAO_LOCAL | DECLARACAO_GLOBAL;

DECLARACAO_LOCAL : 
'declare' VARIAVEL |
'constante' IDENT ':' TIPO_BASICO '=' VALOR_CONSTANTE |
'TIPO' IDENT ':' TIPO;

VARIAVEL :
IDENTIFICADOR (',' IDENTIFICADOR)* ':' TIPO;

IDENTIFICADOR : 
IDENT ('.' IDENT)* DIMENSAO;

DIMENSAO : 
('[' EXP_ARITMETICA ']')*;

TIPO : 
REGISTRO | TIPO_ESTENDIDO;

TIPO_BASICO : 
'literal' | 'inteiro' | 'real' | 'logico';

TIPO_BASICO_IDENT : 
TIPO_BASICO | IDENT;

TIPO_ESTENDIDO : 
('^')? TIPO_BASICO_IDENT;

VALOR_CONSTANTE :
CADEIA | NUM_INT | NUM_REAL | 'verdadeiro' | 'falso';

REGISTRO:
'REGISTRO' (VARIAVEL)* 'fim_REGISTRO';

DECLARACAO_GLOBAL :
'procedimento' IDENT '(' (PARAMETROS)? ')' (DECLARACAO_LOCAL)* (CMD)* 'fim_procedimento' |
'funcao' IDENT '(' (PARAMETROS)? ')' ':' TIPO_ESTENDIDO (DECLARACAO_LOCAL)* (CMD)* 'fim_funcao';

PARAMETRO : 
('var')? IDENTIFICADOR (',' IDENTIFICADOR)* ':' TIPO_ESTENDIDO;

PARAMETROS :
PARAMETRO (',' PARAMETRO)*;

CORPO :
(DECLARACAO_LOCAL)* (CMD)*;

CMD :
CMDLEIA | CMDESCREVA | CMDSE | CMDCASO | CMDPARA | CMDENQUANTO |
CMDFACA | CMDATRIBUICAO | CMDCHAMADA | CMDRETORNE;

CMDLEIA :
'leia' '(' ('^')? IDENTIFICADOR (',' ('^')? IDENTIFICADOR)* ')';

CMDESCREVA :
'escreva' '(' EXPRESSAO (',' EXPRESSAO)* ')';

CMDSE :
'se' EXPRESSAO 'entao' (CMD)* ('senao' (CMD)*)? 'fim_se';

CMDCASO :
'caso' EXP_ARITMETICA 'seja' SELECAO ('senao' (CMD)*)? 'fim_caso';

CMDPARA :
'para' IDENT '<-' EXP_ARITMETICA 'ate' EXP_ARITMETICA 'faca' (CMD)* 'fim_para';

CMDENQUANTO :
'enquanto' EXPRESSAO 'faca' (CMD)* 'fim_enquanto';

CMDFACA :
'faca' (CMD)* 'ate' EXPRESSAO;

CMDATRIBUICAO :
('^')? IDENTIFICADOR '<-' EXPRESSAO;

CMDCHAMADA :
IDENT '(' EXPRESSAO (',' EXPRESSAO)* ')';

CMDRETORNE :
'retorne' EXPRESSAO;

SELECAO :
(ITEM_SELECAO)*;

ITEM_SELECAO :
CONSTANTES ':' (CMD)*;

CONSTANTES :
NUMERO_INTERVALO (',' NUMERO_INTERVALO)*;

NUMERO_INTERVALO :
(OP_UNARIO)? NUM_INT ('..'(OP_UNARIO)? NUM_INT)?;

OP_UNARIO :
'-';

EXP_ARITMETICA :
TERMO (OP1 TERMO)*;

TERMO :
FATOR (OP2 FATOR)*;

FATOR :
PARCELA (OP3 PARCELA)*;

OP1 :
'+' | '-';

OP2 :
'*' | '/';

OP3 :
'%';

PARCELA :
(OP_UNARIO)? PARCELA_UNARIO | PARCELA_NAO_UNARIO;

PARCELA_UNARIO :
('^')? IDENTIFICADOR |
IDENT '(' EXPRESSAO (',' EXPRESSAO)* ')' |
NUM_INT |
NUM_REAL |
'(' EXPRESSAO ')';

PARCELA_NAO_UNARIO :
'&' IDENTIFICADOR | CADEIA;

EXP_RELACIONAL :
EXP_ARITMETICA (OP_RELACIONAL EXP_ARITMETICA)?;

OP_RELACIONAL :
'=' | '<>' | '>=' | '<=' | '>' | '<';

EXPRESSAO :
TERMO_LOGICO (OP_LOGICO_1 TERMO_LOGICO);

TERMO_LOGICO :
FATOR_LOGICO (OP_LOGICO_2 FATOR_LOGICO);

FATOR_LOGICO :
('nao')? PARCELA_logica;

PARCELA_logica:
('verdadeiro' | 'falso') |
EXP_RELACIONAL;

OP_LOGICO_1 :
'ou';


OP_LOGICO_2:
'e';

IDENT : 
('a'..'z'|'A'..'Z' | '_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;

NUM_INT	: ('0'..'9')+;

NUM_REAL	: ('0'..'9')+ ('.' ('0'..'9')+)?;


CADEIA 	: '"' ( ESC_SEQ | ~('"'|'\\'|'\n'|'\r') )* '"'
    ;
CAD_ABERTA 	: '"' ~('"')* ('\n'|'\r')?   
    ;
fragment
ESC_SEQ	: '\\\'';

COMENTARIO
    :   '{' ~('\n'|'\r'|'}')* '\r'? '}' -> skip;
COMENT_ABERTO : '{' ~('\n'|'\r'|'}')* '\r'? ~('}');

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip;
    