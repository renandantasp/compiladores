class SymbolTable:
    def __init__(self, scope):
        self.scope = scope
        self.symbols = {}