import sys

from antlr4 import *
from antlr4.error.Errors import ParseCancellationException

from DNDLexer    import DNDLexer
from DNDParser   import DNDParser
from DNDSemantic import SemanticAnalyzer

#from DNDGenerator import ObjectGenerator


def main(argv):
    
    if len(sys.argv) >= 1:
        input_stream = FileStream(argv[1],"utf-8")
        
        lexer = DNDLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DNDParser(stream)
        tree = parser.program()
        content = tree.toStringTree(recog=parser)
        print(content)
        # sem = SemanticAnalyzer()
        # simb = sem.visitPrograma(tree)
        
        

        
        
        
    else:
        print('Erro: Argumentos inválidos')


if __name__ == '__main__':
    main(sys.argv)
