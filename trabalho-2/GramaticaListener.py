# Generated from Gramatica.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete listener for a parse tree produced by GramaticaParser.
class GramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by GramaticaParser#programa.
    def enterPrograma(self, ctx:GramaticaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#programa.
    def exitPrograma(self, ctx:GramaticaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#declaracoes.
    def enterDeclaracoes(self, ctx:GramaticaParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by GramaticaParser#declaracoes.
    def exitDeclaracoes(self, ctx:GramaticaParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by GramaticaParser#decl_local_global.
    def enterDecl_local_global(self, ctx:GramaticaParser.Decl_local_globalContext):
        pass

    # Exit a parse tree produced by GramaticaParser#decl_local_global.
    def exitDecl_local_global(self, ctx:GramaticaParser.Decl_local_globalContext):
        pass


    # Enter a parse tree produced by GramaticaParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:GramaticaParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by GramaticaParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:GramaticaParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by GramaticaParser#variavel.
    def enterVariavel(self, ctx:GramaticaParser.VariavelContext):
        pass

    # Exit a parse tree produced by GramaticaParser#variavel.
    def exitVariavel(self, ctx:GramaticaParser.VariavelContext):
        pass


    # Enter a parse tree produced by GramaticaParser#identificador.
    def enterIdentificador(self, ctx:GramaticaParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by GramaticaParser#identificador.
    def exitIdentificador(self, ctx:GramaticaParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by GramaticaParser#dimensao.
    def enterDimensao(self, ctx:GramaticaParser.DimensaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#dimensao.
    def exitDimensao(self, ctx:GramaticaParser.DimensaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#tipo.
    def enterTipo(self, ctx:GramaticaParser.TipoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#tipo.
    def exitTipo(self, ctx:GramaticaParser.TipoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#tipo_basico.
    def enterTipo_basico(self, ctx:GramaticaParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#tipo_basico.
    def exitTipo_basico(self, ctx:GramaticaParser.Tipo_basicoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:GramaticaParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by GramaticaParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:GramaticaParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by GramaticaParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:GramaticaParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:GramaticaParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#valor_constante.
    def enterValor_constante(self, ctx:GramaticaParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by GramaticaParser#valor_constante.
    def exitValor_constante(self, ctx:GramaticaParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by GramaticaParser#registro.
    def enterRegistro(self, ctx:GramaticaParser.RegistroContext):
        pass

    # Exit a parse tree produced by GramaticaParser#registro.
    def exitRegistro(self, ctx:GramaticaParser.RegistroContext):
        pass


    # Enter a parse tree produced by GramaticaParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:GramaticaParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by GramaticaParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:GramaticaParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by GramaticaParser#parametro.
    def enterParametro(self, ctx:GramaticaParser.ParametroContext):
        pass

    # Exit a parse tree produced by GramaticaParser#parametro.
    def exitParametro(self, ctx:GramaticaParser.ParametroContext):
        pass


    # Enter a parse tree produced by GramaticaParser#parametros.
    def enterParametros(self, ctx:GramaticaParser.ParametrosContext):
        pass

    # Exit a parse tree produced by GramaticaParser#parametros.
    def exitParametros(self, ctx:GramaticaParser.ParametrosContext):
        pass


    # Enter a parse tree produced by GramaticaParser#corpo.
    def enterCorpo(self, ctx:GramaticaParser.CorpoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#corpo.
    def exitCorpo(self, ctx:GramaticaParser.CorpoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmd.
    def enterCmd(self, ctx:GramaticaParser.CmdContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmd.
    def exitCmd(self, ctx:GramaticaParser.CmdContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdLeia.
    def enterCmdLeia(self, ctx:GramaticaParser.CmdLeiaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdLeia.
    def exitCmdLeia(self, ctx:GramaticaParser.CmdLeiaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdEscreva.
    def enterCmdEscreva(self, ctx:GramaticaParser.CmdEscrevaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdEscreva.
    def exitCmdEscreva(self, ctx:GramaticaParser.CmdEscrevaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdSe.
    def enterCmdSe(self, ctx:GramaticaParser.CmdSeContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdSe.
    def exitCmdSe(self, ctx:GramaticaParser.CmdSeContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdCaso.
    def enterCmdCaso(self, ctx:GramaticaParser.CmdCasoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdCaso.
    def exitCmdCaso(self, ctx:GramaticaParser.CmdCasoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdPara.
    def enterCmdPara(self, ctx:GramaticaParser.CmdParaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdPara.
    def exitCmdPara(self, ctx:GramaticaParser.CmdParaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdEnquanto.
    def enterCmdEnquanto(self, ctx:GramaticaParser.CmdEnquantoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdEnquanto.
    def exitCmdEnquanto(self, ctx:GramaticaParser.CmdEnquantoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdFaca.
    def enterCmdFaca(self, ctx:GramaticaParser.CmdFacaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdFaca.
    def exitCmdFaca(self, ctx:GramaticaParser.CmdFacaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdAtribuicao.
    def enterCmdAtribuicao(self, ctx:GramaticaParser.CmdAtribuicaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdAtribuicao.
    def exitCmdAtribuicao(self, ctx:GramaticaParser.CmdAtribuicaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdChamada.
    def enterCmdChamada(self, ctx:GramaticaParser.CmdChamadaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdChamada.
    def exitCmdChamada(self, ctx:GramaticaParser.CmdChamadaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdRetorne.
    def enterCmdRetorne(self, ctx:GramaticaParser.CmdRetorneContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdRetorne.
    def exitCmdRetorne(self, ctx:GramaticaParser.CmdRetorneContext):
        pass


    # Enter a parse tree produced by GramaticaParser#selecao.
    def enterSelecao(self, ctx:GramaticaParser.SelecaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#selecao.
    def exitSelecao(self, ctx:GramaticaParser.SelecaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#item_selecao.
    def enterItem_selecao(self, ctx:GramaticaParser.Item_selecaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#item_selecao.
    def exitItem_selecao(self, ctx:GramaticaParser.Item_selecaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#constantes.
    def enterConstantes(self, ctx:GramaticaParser.ConstantesContext):
        pass

    # Exit a parse tree produced by GramaticaParser#constantes.
    def exitConstantes(self, ctx:GramaticaParser.ConstantesContext):
        pass


    # Enter a parse tree produced by GramaticaParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:GramaticaParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by GramaticaParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:GramaticaParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by GramaticaParser#op_unario.
    def enterOp_unario(self, ctx:GramaticaParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by GramaticaParser#op_unario.
    def exitOp_unario(self, ctx:GramaticaParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by GramaticaParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:GramaticaParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:GramaticaParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#termo.
    def enterTermo(self, ctx:GramaticaParser.TermoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#termo.
    def exitTermo(self, ctx:GramaticaParser.TermoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#fator.
    def enterFator(self, ctx:GramaticaParser.FatorContext):
        pass

    # Exit a parse tree produced by GramaticaParser#fator.
    def exitFator(self, ctx:GramaticaParser.FatorContext):
        pass


    # Enter a parse tree produced by GramaticaParser#op1.
    def enterOp1(self, ctx:GramaticaParser.Op1Context):
        pass

    # Exit a parse tree produced by GramaticaParser#op1.
    def exitOp1(self, ctx:GramaticaParser.Op1Context):
        pass


    # Enter a parse tree produced by GramaticaParser#op2.
    def enterOp2(self, ctx:GramaticaParser.Op2Context):
        pass

    # Exit a parse tree produced by GramaticaParser#op2.
    def exitOp2(self, ctx:GramaticaParser.Op2Context):
        pass


    # Enter a parse tree produced by GramaticaParser#op3.
    def enterOp3(self, ctx:GramaticaParser.Op3Context):
        pass

    # Exit a parse tree produced by GramaticaParser#op3.
    def exitOp3(self, ctx:GramaticaParser.Op3Context):
        pass


    # Enter a parse tree produced by GramaticaParser#parcela.
    def enterParcela(self, ctx:GramaticaParser.ParcelaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#parcela.
    def exitParcela(self, ctx:GramaticaParser.ParcelaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#parcela_unario.
    def enterParcela_unario(self, ctx:GramaticaParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by GramaticaParser#parcela_unario.
    def exitParcela_unario(self, ctx:GramaticaParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by GramaticaParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:GramaticaParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by GramaticaParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:GramaticaParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by GramaticaParser#exp_relacional.
    def enterExp_relacional(self, ctx:GramaticaParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by GramaticaParser#exp_relacional.
    def exitExp_relacional(self, ctx:GramaticaParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by GramaticaParser#op_relacional.
    def enterOp_relacional(self, ctx:GramaticaParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by GramaticaParser#op_relacional.
    def exitOp_relacional(self, ctx:GramaticaParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by GramaticaParser#expressao.
    def enterExpressao(self, ctx:GramaticaParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#expressao.
    def exitExpressao(self, ctx:GramaticaParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#termo_logico.
    def enterTermo_logico(self, ctx:GramaticaParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#termo_logico.
    def exitTermo_logico(self, ctx:GramaticaParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#fator_logico.
    def enterFator_logico(self, ctx:GramaticaParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#fator_logico.
    def exitFator_logico(self, ctx:GramaticaParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#parcela_logica.
    def enterParcela_logica(self, ctx:GramaticaParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#parcela_logica.
    def exitParcela_logica(self, ctx:GramaticaParser.Parcela_logicaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#op_logico_1.
    def enterOp_logico_1(self, ctx:GramaticaParser.Op_logico_1Context):
        pass

    # Exit a parse tree produced by GramaticaParser#op_logico_1.
    def exitOp_logico_1(self, ctx:GramaticaParser.Op_logico_1Context):
        pass


    # Enter a parse tree produced by GramaticaParser#op_logico_2.
    def enterOp_logico_2(self, ctx:GramaticaParser.Op_logico_2Context):
        pass

    # Exit a parse tree produced by GramaticaParser#op_logico_2.
    def exitOp_logico_2(self, ctx:GramaticaParser.Op_logico_2Context):
        pass


