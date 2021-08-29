import sys
from antlr4 import *
from Gramatica import Gramatica


def main(argv):
    g = Gramatica()
    g.token_label = {     1:'PALAVRA_CHAVE',
                        2:'NUMINT',
                        3:'IDENT',
                        4:'CADEIA',
                        5:'COMENTARIO',
                        6:'WS',
                        7:'OP_EL',
                        8:'OP_ARIT',
                        9:'DELIM',
                        10:'ABREPAR',
                        11:'FECHAPAR',               
                                }
                                
    if len(sys.argv) > 2:
        inp = FileStream(argv[1],"utf-8")
        lex = Gramatica(inp)
        lex.token_label = {     1:'PALAVRA_CHAVE',
                        2:'NUMINT',
                        3:'IDENT',
                        4:'CADEIA',
                        5:'COMENTARIO',
                        6:'WS',
                        7:'OP_EL',
                        8:'OP_ARIT',
                        9:'DELIM',
                        10:'ABREPAR',
                        11:'FECHAPAR',               
                                }
        stream = CommonTokenStream(lex)
        t = lex.nextToken()
        while t.type != Token.EOF:
            if t.type in [1,9,10,11]:
            	with open(argv[2], 'a') as f:
            		f.write('<\'' + t.text + '\',\'' + t.text + '\'>')
                #print('<\'' + t.text + '\',\'' + t.text + '\'>')
            else:
            	with open(argv[2], 'a') as f:
            		f.write('<\'' + t.text + ',\'' + lex.token_label[t.type] + '\'>')
                #print('<\'' + t.text + ',\'' + lex.token_label[t.type] + '\'>')
            t = lex.nextToken()

        
        
    else:
        inp = InputStream(sys.stdin.readline())


if __name__ == '__main__':
    main(sys.argv)
