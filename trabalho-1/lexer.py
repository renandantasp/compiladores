import sys
from antlr4 import *
from Gramatica import Gramatica


def main(argv):
    if len(sys.argv) >= 3:
        entrada = FileStream(argv[1],"utf-8")
        lex = Gramatica(entrada)
        lex.removeErrorListeners() #remove o verificador de erros pois fazemos as verificaçoes na mao
        lex.token_label = {
                    1:'PALAVRA_CHAVE', #
                    2:'TIPO', #
                    3:'CADEIA',
                    4:'CAD_ABERTA',
                    5:'COMENTARIO',
                    6:'COMENT_ABERTO',
                    7:'WS',
                    8:'NUM_INT',
                    9:'NUM_REAL',
                    10:'OP', #
                    11:'OP_LOGIC', #
                    12:'IDENT',
                    13:'SIMBOLO', #
                    14:'ESCOPO' #
}
    
        stream = CommonTokenStream(lex)
        t = lex.nextToken()
        
       
        f = open(argv[2],'w')
        while t.type != Token.EOF:
            if t.type in [1,2,10,11,13,14]: #Regras para tokens proprios 
                f.write('<\'' + t.text + '\',\'' + t.text + '\'>\n')
                
            elif t.type == 15:#procura por simbolos que nao foram definidos
                f.write('Linha ' + str(t.line) + ': ' + str(t.text) + ' - simbolo nao identificado\n')
                f.close()
                break

            # Verifica por '{' e '"' nao fechados
            elif t.type == 6:
            	f.write('Linha ' + str(t.line) + ': comentario nao fechado\n')
            	f.close()
            	break
            elif t.type == 4:
                f.write('Linha ' + str(t.line) + ': cadeia literal nao fechada\n')
                f.close()
                break
            else:
                f.write('<\'' + t.text + '\',' + lex.token_label[t.type] + '>\n')
            
            t = lex.nextToken()
            
        f.close()
        
        
    else:
        print('Erro: Argumentos inválidos')


if __name__ == '__main__':
    main(sys.argv)
