from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class ThrowingErrorListener(ErrorListener):
    def __init__(self, filename):
        self.filename = filename
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        t = offendingSymbol.text.replace('<EOF>','EOF')
        token = offendingSymbol.type
        # Erros apontados pelo analisador lexico
        if token == 64:
            ex = f'Linha {line}: cadeia literal nao fechada\nFim da compilacao\n'
            f = open(self.filename,'w')
            f.write(ex)
            f.close()
            ex = ParseCancellationException(f'Linha {line}: cadeia literal nao fechada\n')
            ex.line = line
            raise ex #Sobe sinal de erro de forma a parar a analise do resto do programa

        elif token == 66:
           ex = f'Linha {line}: comentario nao fechado\nFim da compilacao\n'
           f = open(self.filename,'w')
           f.write(ex)
           f.close()
           ex = ParseCancellationException(f'Linha {line}: comentario nao fechado\nFim da compilacao\n')
           ex.line = line
           raise ex

        elif token == 68:
            ex = f'Linha {line}: {t} - simbolo nao identificado\nFim da compilacao\n'
            f = open(self.filename,'w')
            f.write(ex)
            f.close()
            ex = ParseCancellationException(f'Linha {line}: {t} - simbolo nao identificado\nFim da compilacao\n')
            ex.line = line 
            ex.t = t
            raise ex

        # Erros sintaticos
        else:
            ex = f'Linha {line}: erro sintatico proximo a {t}\nFim da compilacao\n'
            f = open(self.filename,'w')
            f.write(ex)
            f.close()
            ex = ParseCancellationException(f'Linha {line}: erro sintatico proximo a {t}\n')
            ex.line = line
            ex.t = t
            raise ex

        
        