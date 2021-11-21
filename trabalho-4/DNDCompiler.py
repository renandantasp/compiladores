import sys

from antlr4 import *
from antlr4.error.Errors import ParseCancellationException

from DNDLexer    import DNDLexer
from DNDParser   import DNDParser
from DNDSemantic import SemanticAnalyzer
from utils       import ErrorHandler
#from DNDGenerator import ObjectGenerator


def main(argv):
    err = ErrorHandler()
    try:
        input_stream = FileStream(argv[1],"utf-8")
        lexer = DNDLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DNDParser(stream)
        tree = parser.program()

    except ParseCancellationException as p:
        err.writeError(f"Erro: {p}")

    except IndexError:
        err.writeError('Erro: Argumentos inválidos')
    
    if not err.hasError():
        sem = SemanticAnalyzer(err)
        simb = sem.visitProgram(tree)
        if not err.hasError():
            print(simb)
        #content = tree.toStringTree(recog=parser)
    err.showError()


if __name__ == '__main__':
    main(sys.argv)
