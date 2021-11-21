from antlr4 import *
from DNDParser import DNDParser
from DNDVisitor  import DNDVisitor
from utils import *

class SemanticAnalyzer(DNDVisitor):
    def __init__(self, err:ErrorHandler):
        self.scopes = {}
        self.error = ""
        self.valid = True
        self.err = err

    def outputHandler(self):
        # spell = self.scopes['spell']
        # id = spell.symbols['id']
        # print("spell: " + id)
        # print(f"\t {id}.level  : {str(spell.symbols['level'])}")
        # print(f"\t {id}.name   : {str(spell.symbols['name'])}")
        # print(f"\t {id}.school : {str(spell.symbols['school'])}")
        # print(f"\t {id}.descr  : {str(spell.symbols['descr'])}")
        print("cria tabela de simbolo ô buceta.")

        return ':)'
    
    def visitProgram(self, ctx:DNDParser.ProgramContext):
      #'def' IDENT '{' tags '}'
        self.scopes['spell'] = SymbolTable('spell')
        self.scopes['spell'].symbols['id'] = str(ctx.IDENT())
        self.scopes['spell'].symbols['level']  = 0
        self.scopes['spell'].symbols['name']   = ''
        self.scopes['spell'].symbols['school'] = ''
        self.scopes['spell'].symbols['descr']  = ''
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
            self.scopes['spell'].symbols['level'] = num_int

    def visitName_tag(self, ctx:DNDParser.Name_tagContext):
        self.scopes['spell'].symbols['name'] = str(ctx.STRING()).replace("\"", "")


    def visitSchool_tag(self, ctx:DNDParser.School_tagContext):
        self.scopes['spell'].symbols['school'] = str(ctx.SCHOOL())

    def visitDescr_tag(self, ctx:DNDParser.Descr_tagContext):
        self.scopes['spell'].symbols['descr'] = str(ctx.STRING()).replace("\"", "")
