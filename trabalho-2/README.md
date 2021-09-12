## Trabalho 2 - Analisador Sintático
---

## Instruções para Execução

### Gerando a gramática
```
antlr4 -Dlanguage=python3 Gramatica.g4
```
### Rodando o analisador sintático 
```
python3 parser.py <arquivo de entrada> <arquivo de saida>
```
---
## Instruções para Teste
* Executando as linhas abaixo, vão ser gerados na pasta out os resultados do analisador sintático (os erros sintáticos também serão impressos na execução do programa, mas não afetará os arquivos de saída):
```
chmod + x run
./run
```
* E para comparar os resultados, executar as linhas abaixo. Se os resultados derem iguais, está correto, senão, está errado
```
chmod + x diff
./diff
```
