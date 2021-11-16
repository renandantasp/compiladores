grammar DND;

program:
body;

body: 
(spell)*;

spell: 
'def' IDENT '{' (tags) '}';

tags:
level_tag  ',' 
name_tag   ',' 
school_tag ',' 
descr_tag   ;

level_tag:
'LEVEL' SEP NUM_INT; 

name_tag:
'NAME' SEP STRING;

school_tag:
'SCHOOL' SEP SCHOOL;

descr_tag:
'DESCR' SEP STRING;

cast_tag:
'CAST' SEP '(' NUM_INT ',' CAST_TIME ')';

range_tag:
'RANGE' SEP ((NUM_REAL)? STRING);


/*============================ LEX RULES ============================*/


// Variavel, Strings e Valores Numericos


NUM_INT	: 
('0'..'9')+;

NUM_REAL : 
('0'..'9')+ ('.' ('0'..'9')+)?;

STRING 	: 
'"' ( ESC_SEQ | ~('"'|'\\'|'\n'|'\r') )* '"';

OPEN_STRING 	: 
'"' ~('"')* ('\n'|'\r')?;

fragment
ESC_SEQ	: '\\\'';


// Comentarios e White Space

COMENT :   
'[' ~('\n'|'\r'|'[')* '\r'? ']' -> skip;

COMENT_ABERTO : 
'/*' ~('}')*;

WS  :   
( ' ' | '\t' | '\r' | '\n' ) -> skip;


// Regras Específicas

SEP :
':';


CAST_TIME :
'Action' | 'Reaction' | 'Bonus Action' ;

SCHOOL :
'Abjuration'  | 'Conjuration'   | 'Divination' |
'Enchantment' | 'Evocation'     | 'Illusion'   |
'Necromancy'  | 'Transmutation' ;


IDENT : 
('a'..'z'|'A'..'Z' | '_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;
