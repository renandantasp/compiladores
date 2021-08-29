## Trabalho 1 - Analisador Léxico
---

## Instruçoes para Execuçao
### Dependencias 
* Antlr4
```
$ cd /usr/local/lib
$ curl -O https://www.antlr.org/download/antlr-4.9-complete.jar 
```
* Adicionar Antlr4 para o ```ClassPath```:
```
$ export CLASSPATH=".:/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH"
```
* Criar Aliases para o Antlr:
```
$ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
$ alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
```

* Antlr4-python3-runtime
```
sudo pip install antlr4-python3-runtime==<version>
```
*deve ser verificado a versao do antlr4. Para isso, rode o comando:*
```
pip freeze | grep antlr
```
### Gerando a gramatica
```
antlr4 -Dlanguage=python3 Gramatica.g4
```
### Rodando o analisador lexico 
```
python3 lexer.py <arquivo de entrada> <arquivo de saida> 
