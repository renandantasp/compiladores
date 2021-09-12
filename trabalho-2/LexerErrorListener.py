from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class ThrowingErrorListener(ErrorListener):
    def __init__(self, filename='tmp.txt'):
        self.filename = filename
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        t = offendingSymbol
        ex = f'Linha {line}: erro sintatico proximo auuuuu {t}\nFim da compilacao\n'
        f = open(self.filename,'w')
        f.write(ex)
        f.close()

        #ex = ParseCancellationException(f'Linha {line}: {column} {msg}')