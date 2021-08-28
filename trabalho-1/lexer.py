import sys
from antlr4 import *
from Gramatica import Gramatica


def main(argv):
    g = Gramatica()

    if len(sys.argv) > 1:
        inp = FileStream(argv[1],"utf-8")
        lex = Gramatica(inp)
        stream = CommonTokenStream(lex)
        t = lex.nextToken()
        while t.type != Token.EOF:
            if t.type in [1,9,10,11]:
                print('<\'' + t.text + '\',\'' + t.text + '\'>')
            else:
                print('<\'' + t.text + ',\'' + lex.token_label[t.type] + '\'>')
            t = lex.nextToken()

        
        
    else:
        inp = InputStream(sys.stdin.readline())


if __name__ == '__main__':
    main(sys.argv)
