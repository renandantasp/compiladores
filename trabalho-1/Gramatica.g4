lexer grammar Gramatica;

PALAVRA_CHAVE 
	:	'escreva' | 'leia' | 'fim_algoritmo' | 'algoritmo' |'declare' | 'para' | 'ate' | 'faca' |'fim_para'
    | 'enquanto' | 'fim_enquanto' |'registro' | 'fim_registro' | 'procedimento' | 'var' | 'fim_procedimento'
    | 'funcao' | 'fim_funcao' | 'tipo' | 'retorne' | 'constante'; 

TIPO : 'inteiro' | 'literal' | 'real' | 'logico'
    ;

CADEIA 	: '"' ( ESC_SEQ | ~('"'|'\\') )* '"'
    ;
CAD_ABERTA 	: '"' ~('"')* ('\n'|'\r')   
    ;

fragment
ESC_SEQ	: '\\\'';
COMENTARIO
    :   '{' ~('\n'|'\r')* '\r'? '}' -> skip;
COMENT_ABERTO : '{' ~('}')*;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip;
    
NUMINT	: ('0'..'9')+;

NUMREAL	: ('0'..'9')+ ('.' ('0'..'9')+)?;

OP	:	'+' | '-' | '/' | '*' | '<-' | '..' | '<>' | '%' |'^' | '&'
	;

OP_LOGIC : 'e' | 'ou' | 'nao' | '>' | '<' | '=' | '<=' | '>=' | 'se' | 'senao' | 'fim_se' | 'entao' | 'caso' | 'seja' | 'fim_caso'
    | 'falso'   | 'verdadeiro'
    ;

IDENT : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;


SIMBOLO	:	':' | ',' | '.'
	;
ESCOPO :	'(' | ')' | '[' | ']'
	;

