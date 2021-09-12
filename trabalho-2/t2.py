import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from ThrowingErrorListener import ThrowingErrorListener
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from GramaticaListener import GramaticaListener


def main(argv):
    
    if len(sys.argv) >= 3:
        input_stream = FileStream(argv[1],"utf-8")
        lexer = GramaticaLexer(input_stream)
        lexer.removeErrorListeners()
        stream = CommonTokenStream(lexer)
        parser = GramaticaParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ThrowingErrorListener(filename=argv[2]))
        tree = parser.programa()
        
        
    else:
        print('Erro: Argumentos inválidos')


if __name__ == '__main__':
    main(sys.argv)
