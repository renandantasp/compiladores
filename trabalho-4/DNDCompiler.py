import sys

from antlr4 import *
from antlr4.error.Errors import ParseCancellationException

from DNDLexer    import DNDLexer
from DNDParser   import DNDParser
from DNDSemantic import SemanticAnalyzer
from DNDGenerator import PageGenerator
from utils       import ErrorHandler
from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener( ErrorListener ):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print (str(line) + ":" + str(column) + ": sintax ERROR, " + str(msg))
        print ("Terminating Translation")
        sys.exit()

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print ("Ambiguity ERROR, " + str(configs))
        sys.exit()

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print ("Attempting full context ERROR, " + str(configs))
        sys.exit()

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print ("Context ERROR, " + str(configs))
        sys.exit()
    
def main(argv):
    err = ErrorHandler()
    try:
        input_stream = FileStream(argv[1],"utf-8")
        lexer = DNDLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DNDParser(stream)
        parser._listeners = [ MyErrorListener() ]
        tree = parser.program()

    except ParseCancellationException as p:
        err.writeError(f"Erro: {p}")

    except IndexError:
        err.writeError('Erro: Argumentos inválidos')
    
    if not err.hasError():
        sem = SemanticAnalyzer(err)
        sem.visitProgram(tree)
        symbols = sem.outputHandler()
        if not err.hasError():
            if len(argv) >= 3:
                pg_gen = PageGenerator(symbols, argv[2])
            else:
                pg_gen = PageGenerator(symbols,"result")

            pg_gen.createPage()
    err.showError()


if __name__ == '__main__':
    main(sys.argv)
