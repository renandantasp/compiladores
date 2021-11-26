import sys, os

from antlr4 import *
from antlr4.error.Errors import ParseCancellationException

from DNDLexer    import DNDLexer
from DNDParser   import DNDParser
from DNDSemantic import SemanticAnalyzer
from DNDGenerator import PageGenerator
from utils       import ErrorHandler
from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener( ErrorListener ):
    def __init__(self,err:ErrorHandler):
        self.err = err

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.err.writeError (f"Line {str(line)}: { str(msg)}")


    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        self.err.writeError ("Ambiguity ERROR, " + str(configs))

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        self.err.writeError ("Attempting full context ERROR, " + str(configs))

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        self.err.writeError ("Context ERROR, " + str(configs))
    
def main(argv):
    err = ErrorHandler()
    try:
        input_stream = FileStream(argv[1],"utf-8")
        lexer = DNDLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DNDParser(stream)
        parser._listeners = [ MyErrorListener(err) ]
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
    
    if err.hasError():
        error = err.showError()
        if len(argv) >=3:
            if not os.path.isdir(argv[2]):
                os.mkdir(argv[2])
            with open(f"{argv[2]}/error_log.txt", "w") as f:
                f.write(error)
        else:
            if not os.path.isdir("result"):
                os.mkdir("result")
            with open(f"result/error_log.txt", "w") as f:
                f.write(error) 


if __name__ == '__main__':
    main(sys.argv)
