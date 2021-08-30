## Trabalho 1 - Analisador Léxico
---

## Instruções para Execução
### Dependências 
* Download Antlr4
```
$ cd /usr/local/lib
$ curl -O https://www.antlr.org/download/antlr-4.9-complete.jar 
```
* Adicionar o Antlr4 para o ```ClassPath```:
```
$ export CLASSPATH=".:/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH"
```
* Criar aliases para o Antlr:
```
$ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
$ alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
```

* Antlr4-python3-runtime (a versão do pip deve ser a mesma do Antlr)
```
sudo pip install antlr4-python3-runtime==<versão do Antlr instalada>
```

### Gerando a gramática
```
antlr4 -Dlanguage=python3 Gramatica.g4
```
### Rodando o analisador léxico 
```
python3 lexer.py <arquivo de entrada> <arquivo de saida>
```
---
## Instruções para Teste
* Executando as linhas abaixo, vão ser gerados na pasta out os resultados do analisador léxico:
```
chmod + x run
./run
```
* E para comparar os resultados, executar as linhas abaixo. Se os resultados derem iguais, está correto, senão, está errado
```
chmod + x diff
./diff
```
