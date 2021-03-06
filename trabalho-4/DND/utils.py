class SymbolTable:
    def __init__(self, scope):
        self.scope = scope
        self.symbol = {}

    def get_symbols(self):
        return self.symbol

class ErrorHandler:
    def __init__(self):
        self.error = False
        self.message = ""

    def hasError(self):
        return self.error

    def writeError(self, msg=""):
        self.error = True
        self.message = f"{self.message}{msg}\n"
    
    def showError(self):
        return self.message
