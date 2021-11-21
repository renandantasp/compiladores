from antlr4 import *
from DNDParser import DNDParser
from DNDVisitor  import DNDVisitor
from utils import *

class SemanticAnalyzer(DNDVisitor):
    def __init__(self):
        self.scopes = {}
        self.error = ""
        self.valid = True
    
    def visitProgram(self, ctx:DNDParser.ProgramContext):
      #'def' IDENT '{' tags '}'
        self.scopes['spell'] = SymbolTable('spell')
        self.scopes['spell'].symbols['level']  = 0
        self.scopes['spell'].symbols['name']   = ''
        self.scopes['spell'].symbols['school'] = ''
        self.scopes['spell'].symbols['descr']  = ''
        if self.valid:
            self.visitTags(ctx.tags())
            return self #metodo para output
        return None

    

        