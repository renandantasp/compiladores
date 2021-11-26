from antlr4 import *
from DNDParser import DNDParser
from DNDVisitor  import DNDVisitor
from utils import *

class SemanticAnalyzer(DNDVisitor):
    def __init__(self, err:ErrorHandler):
        self.scopes = []
        self.actual_scope = ''
        self.table = {}
        self.variables = {}
        self.err = err

    def outputHandler(self):
        ret = {}            
        for scope in self.scopes:
            ret[scope] = {}
            for key, value in self.table[scope].symbol.items():
                ret[scope][key] = value
        for spell, content in ret.items():
            for key, value in content.items():
                print(key,'\t:', value)
        return ret
    
   # def visitDeclaracao(self, ctx:DNDParser.DeclaracaoContext):
   #     self.actual_scope = 'decl'
   #     self.scopes.append('decl')
        
   #     self.table['decl'] = SymbolTable('decl')
   #     return self.visitChildren(ctx)
        #print(ctx.decl()
        #self.visitDecl(ctx.decl())
        # if self.err.hasError():
        #     return None


    def visitDecl(self, ctx:DNDParser.DeclContext):
        if str(ctx.IDENT()) in self.variables.keys():
            self.err.writeError(f"Linha {ctx.start.line}: não pode haver duas variaveis com o mesmo nome.")
        else:
            if str(ctx.DECL_TYPE()) != 'int':
                if ctx.STRING():
                    self.variables[str(ctx.IDENT())] = { 'type' : str(ctx.DECL_TYPE()),
                                                        'value': str(ctx.STRING()).replace("\"", "")}
                else:
                    self.err.writeError(f"Linha {ctx.start.line}: variaveis do tipo {str(ctx.DECL_TYPE())} não podem receber valores inteiros.")
            else:
                try:
                    self.variables[str(ctx.IDENT())] = {  'type' : str(ctx.DECL_TYPE()),
                                                        'value': int(str(ctx.NUM_INT()))}
                except:
                    self.err.writeError(f"Linha {ctx.start.line}: variaveis inteiras não podem receber string.")


        # print(self.variables)
    
    def visitSpell(self, ctx:DNDParser.SpellContext):
      #'def' IDENT '{' tags '}'
        
        spell =  str(ctx.IDENT())
        if spell in self.scopes:
            self.err.writeError(f"Linha {ctx.start.line}: não pode haver dois spells com mesmo identificador.")
            return None
        self.scopes.append(spell)
        self.actual_scope = spell
        self.table[spell] = SymbolTable(spell)
        self.visitTags(ctx.tags())
        if self.err.hasError():
            return None
        #if self.actual_scope != '0decl':
        #    return self.outputHandler()

    
    def visitLevel_tag(self, ctx:DNDParser.Level_tagContext):
       #'LEVEL' SEP NUM_INT
        if ctx.NUM_INT():
            num_int = int(str(ctx.NUM_INT()))
        else:
            varname = str(ctx.IDENT())
            if varname in self.variables.keys():
                if self.variables[varname]['type'] == 'int':
                    num_int = self.variables[varname]['value']
                else:
                    self.err.writeError(f"Linha {ctx.start.line}: campo LEVEL só pode receber variavel do tipo int. Passado: {self.variables[varname]['type']}")        
                    return
            else:
                self.err.writeError(f"Linha {ctx.start.line}: variável passada não existe.")        
                return


        if num_int < 1:
            self.err.writeError(f"Linha {ctx.start.line}: valor de level não pode ser menor do que 0.")        
        else:
            self.table[self.actual_scope].symbol['level'] = num_int


    def visitName_tag(self, ctx:DNDParser.Name_tagContext):
      #'NAME' SEP NUM_INT; 
        if ctx.STRING():
            self.table[self.actual_scope].symbol['name'] = str(ctx.STRING()).replace("\"", "")
            return
        varname = str(ctx.IDENT())
        if varname in self.variables.keys():
            if self.variables[varname]['type'] == 'text':
                self.table[self.actual_scope].symbol['name'] = self.variables[varname]['value']
            else:
                self.err.writeError(f"Linha {ctx.start.line}: campo descr só pode receber variavel do tipo text. Passado: {self.variables[varname]['type']}")        
        else:
            self.err.writeError(f"Linha {ctx.start.line}: variável passada não existe.")   
    

    def visitSchool_tag(self, ctx:DNDParser.School_tagContext):
       #'SCHOOL' SEP SCHOOL;
        if ctx.SCHOOL():
            self.table[self.actual_scope].symbol['school'] = str(ctx.SCHOOL())
            return
        if str(ctx.IDENT()) in self.variables.keys():
            var = self.variables[str(ctx.IDENT())]
            if var['type'] == 'school':
                self.table[self.actual_scope].symbol['school'] = var['value']
            else:
                self.err.writeError(f"Linha {ctx.start.line}: campo school só pode receber variavel do tipo school. Passado: {var['type']}")        
        else:
            self.err.writeError(f"Linha {ctx.start.line}: variável passada não existe.")        


    def visitDescr_tag(self, ctx:DNDParser.Descr_tagContext):
       #'DESCR' SEP STRING;
        if ctx.STRING():
            self.table[self.actual_scope].symbol['descr'] = str(ctx.STRING()).replace("\"", "")
            return
        varname = str(ctx.IDENT())
        if varname in self.variables.keys():
            if self.variables[varname]['type'] == 'text':
                self.table[self.actual_scope].symbol['descr'] = self.variables[varname]['value']
            else:
                self.err.writeError(f"Linha {ctx.start.line}: campo descr só pode receber variavel do tipo text. Passado: {self.variables[varname]['type']}")        
        else:
            self.err.writeError(f"Linha {ctx.start.line}: variável passada não existe.")        
        
    def visitDamage_tag(self, ctx:DNDParser.Damage_tagContext):
        if 'damage' in self.table[self.actual_scope].symbol:
            self.err.writeError(f"Linha {ctx.start.line}: tag DAMAGE já foi inserida.")
        else:
            self.table[self.actual_scope].symbol['damage'] = str(ctx.NUM_INT()) + str(ctx.DICE())

    def visitDamage_type_tag(self, ctx:DNDParser.Damage_type_tagContext):
        if 'dmg_type' in self.table[self.actual_scope].symbol:
            self.err.writeError(f"Linha {ctx.start.line}: tag DMG_TYPE já foi inserida.")
        else:
            self.table[self.actual_scope].symbol['dmg_type'] = str(ctx.STRING())

    def visitCast_tag(self, ctx:DNDParser.Cast_tagContext):
        if 'cast' in self.table[self.actual_scope].symbol:
            self.err.writeError(f"Linha {ctx.start.line}: tag CAST já foi inserida.")
        else:
            self.table[self.actual_scope].symbol['cast'] = str(ctx.NUM_INT()) + ' ' + str(ctx.CAST_TIME())

    def visitComp_tag(self, ctx:DNDParser.Comp_tagContext):
        if 'comp' in self.table[self.actual_scope].symbol:
            self.err.writeError(f"Linha {ctx.start.line}: tag COMP já foi inserida.")
        else:
            print("hhhhh")