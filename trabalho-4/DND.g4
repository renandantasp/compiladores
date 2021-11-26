grammar DND;

program:
(declaracao) (spell)*;

declaracao:
'decl:' (decl)* | ;


decl:
DECL_TYPE   IDENT '=' (STRING | NUM_INT)  ';' ;


spell:
'def' IDENT '{' tags '}';

tags:
level_tag  ',' 
name_tag   ',' 
school_tag ','
descr_tag   ;

level_tag:
'LEVEL' SEP (NUM_INT | IDENT); 

name_tag:
'NAME' SEP (STRING | IDENT);

school_tag:
'SCHOOL' SEP (SCHOOL | IDENT);

descr_tag:
'DESCR' SEP (STRING | IDENT);

damage_tag:
'DAMAGE' SEP ((NUM_INT DICE) | (IDENT DICE));

// cast_tag:
// 'CAST' SEP '(' NUM_INT ',' CAST_TIME ')';




/*============================ LEX RULES ============================*/

// Variavel, Strings e Valores Numericos
NUM_INT	: 
('-')? ('0'..'9')+;

NUM_REAL : 
('-')? ('0'..'9')+ ('.' ('0'..'9')+)?;

STRING 	: 
'"' ( ESC_SEQ | ~('"'|'\\'|'\n'|'\r') )* '"';

OPEN_STRING 	: 
'"' ~('"')* ('\n'|'\r')?;

fragment
ESC_SEQ	: '\\\'';


// Skips
COMMENT :   
'%' ~('\n'|'\r')* '\r'? '\n' -> skip;

WS  :   
( ' ' | '\t' | '\r' | '\n' ) -> skip;


// Regras Específicas

SEP :
':';


CAST_TIME :
'Action' | 'Reaction' | 'Bonus Action' | 'Minute' | 'Hour';

SCHOOL :
'Abjuration'  | 'Conjuration'   | 'Divination' |
'Enchantment' | 'Evocation'     | 'Illusion'   |
'Necromancy'  | 'Transmutation' ;

DECL_TYPE :
'school' | 'dmg' | 'desc' | 'int';

DICE:
'D4'  | 'D6'  | 'D8' | 
'D10' | 'D12' | 'D20';


IDENT : 
('a'..'z'|'A'..'Z' | '_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;
