lexer grammar Gramatica;

PALAVRA_CHAVE 
	:	'algoritmo' | 'declare' | 'leia' | 'escreva' | 'fim_algoritmo' | 'literal' | 'inteiro'; 

NUMINT	: ('+'|'-')?('0'..'9')+;

//NUMREAL	: ('+'|'-')?('0'..'9')+ ('.' ('0'..'9')+)?;

VARIAVEL : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9')*;

CADEIA 	: '"' ( ESC_SEQ | ~('"'|'\\') )* '"';

fragment
ESC_SEQ	: '\\\'';
COMENTARIO
    :   '{' ~('\n'|'\r')* '\r'? '}\n' -> skip;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip;
    
OP_REL	:	'>' | '>=' | '<' | '<=' | '<>' | '='
	;
OP_ARIT	:	'+' | '-' | '*' | '/'
	;
DELIM	:	':' | ','
	;
ABREPAR :	'('
	;
FECHAPAR:	')'
	;