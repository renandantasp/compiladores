## Trabalho 1 - Analisador Léxico
---

## Instruçoes para Execuçao
### Dependencias 
* Antlr4
```
$ cd /usr/local/lib
$ curl -O https://www.antlr.org/download/antlr-4.9-complete.jar 
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
