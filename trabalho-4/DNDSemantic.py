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
        tmp = self.table[self.actual_scope]
        # id = self.actual_scope
        # print(f"\t {id}.level  : {str(tmp.symbol['level'])}")
        # print(f"\t {id}.name   : {str(tmp.symbol['name'])}")
        # print(f"\t {id}.school : {str(tmp.symbol['school'])}")
        # print(f"\t {id}.descr  : {str(tmp.symbol['descr'])}")
        return [self.scopes, self.table]
        #return self.table[self.actual_scope].symbol['level']
        #return ':)'
    
    def visitProgram(self, ctx:DNDParser.ProgramContext):
      #'def' IDENT '{' tags '}'
        spell =  str(ctx.IDENT())
        self.scopes.append(spell)
        self.actual_scope = spell
        self.table[spell] = SymbolTable(spell)
 
        self.table[spell].symbol['level']  = 0
        # self.scopes['spell'].symbols['id'] = str(ctx.IDENT())
        # self.scopes['spell'].symbols['level']  = 0
        # self.scopes['spell'].symbols['name']   = ''
        # self.scopes['spell'].symbols['school'] = ''
        # self.scopes['spell'].symbols['descr']  = ''
        if self.valid:

            self.visitTags(ctx.tags())

            if self.err.hasError():
                return None
            return self.outputHandler()

    
    def visitLevel_tag(self, ctx:DNDParser.Level_tagContext):
        num_int = int(str(ctx.NUM_INT()))
        if num_int < 1:
            self.err.writeError(f"Linha {ctx.start.line}: valor de level não pode ser menor do que 0.")        
        else:
            self.table[self.actual_scope].symbol['level'] = num_int

    def visitName_tag(self, ctx:DNDParser.Name_tagContext):
       self.table[self.actual_scope].symbol['name'] = str(ctx.STRING()).replace("\"", "")


    def visitSchool_tag(self, ctx:DNDParser.School_tagContext):
        self.table[self.actual_scope].symbol['school'] = str(ctx.SCHOOL())

    def visitDescr_tag(self, ctx:DNDParser.Descr_tagContext):
        self.table[self.actual_scope].symbol['descr'] = str(ctx.STRING()).replace("\"", "")
