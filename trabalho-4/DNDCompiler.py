import sys
from antlr4 import *
from DNDLexer    import DNDLexer
from DNDParser   import DNDParser
#from DNDVisitor  import DNDVisitor

from DNDSemantic import SemanticAnalyzer
#from DNDGenerator import ObjectGenerator


def main(argv):
    
    if len(sys.argv) >= 1:
        input_stream = FileStream(argv[1],"utf-8")
        
        lexer = DNDLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DNDParser(stream)
        tree = parser.program()
        #ast = DNDVisitor().visitPrograma(tree)
        

        
        
        
    else:
        print('Erro: Argumentos inválidos')


if __name__ == '__main__':
    main(sys.argv)
