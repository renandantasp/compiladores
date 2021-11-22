from antlr4 import *
from DNDParser import DNDParser
from DNDVisitor  import DNDVisitor
from utils import *

class SemanticAnalyzer(DNDVisitor):
    def __init__(self, err:ErrorHandler):
        self.scopes = []
        self.actual_scope = ''
        self.table = {}
        self.valid = True
        self.err = err

    def outputHandler(self):
        ret = {}
        for scope in self.scopes:
            ret[scope] = {}
            for key, value in self.table[scope].symbol.items():
                ret[scope][key] = value
        return ret
    
    def visitProgram(self, ctx:DNDParser.ProgramContext):
      #'def' IDENT '{' tags '}'
        spell =  str(ctx.IDENT())
        self.scopes.append(spell)
        self.actual_scope = spell
        self.table[spell] = SymbolTable(spell)
 
        self.table[spell].symbol['level']  = 0
        if self.valid:
            self.visitTags(ctx.tags())
            if self.err.hasError():
                return None
            return self.outputHandler()

    
    def visitLevel_tag(self, ctx:DNDParser.Level_tagContext):
       #'LEVEL' SEP NUM_INT
        num_int = int(str(ctx.NUM_INT()))
        if num_int < 1:
            self.err.writeError(f"Linha {ctx.start.line}: valor de level não pode ser menor do que 0.")        
        else:
            self.table[self.actual_scope].symbol['level'] = num_int


    def visitName_tag(self, ctx:DNDParser.Name_tagContext):
      #'NAME' SEP NUM_INT; 
       self.table[self.actual_scope].symbol['name'] = str(ctx.STRING()).replace("\"", "")

    def visitSchool_tag(self, ctx:DNDParser.School_tagContext):
       #'SCHOOL' SEP SCHOOL;
        self.table[self.actual_scope].symbol['school'] = str(ctx.SCHOOL())

    def visitDescr_tag(self, ctx:DNDParser.Descr_tagContext):
       #'DESCR' SEP STRING;
        self.table[self.actual_scope].symbol['descr'] = str(ctx.STRING()).replace("\"", "")
