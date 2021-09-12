import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from ThrowingErrorListener import ThrowingErrorListener
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from GramaticaListener import GramaticaListener


def main(argv):
    
    if len(sys.argv) >= 3:
        #le o arquivo de entrada
        input_stream = FileStream(argv[1],"utf-8")
        
        #passa o arquivo pelo analisador lexico
        lexer = GramaticaLexer(input_stream)
        
        #remove o listener de erros do analisador lexico
        lexer.removeErrorListeners()
        stream = CommonTokenStream(lexer)

        #passa o arquivo tokenizado pelo analisador sintatico
        parser = GramaticaParser(stream)

        #remove o listener de erros do analisador sintatico e adiciona
        #um feito especificamente para a aplicação
        parser.removeErrorListeners()
        parser.addErrorListener(ThrowingErrorListener(filename=argv[2]))
        
        #roda o arquivo a partir da regra inicial 'programa'
        tree = parser.programa()
        
        
    else:
        print('Erro: Argumentos inválidos')


if __name__ == '__main__':
    main(sys.argv)
