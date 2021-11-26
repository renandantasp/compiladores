## Trabalho 4 - Linguagem DND
---
## 1  A Linguagem DND


## 2  Instruções para Execução
### 2.1  Dependências 
* Download Antlr4
```
cd /usr/local/lib
curl -O https://www.antlr.org/download/antlr-4.9-complete.jar 
```
* Adicionar o Antlr4 para o ```ClassPath```:
```
export CLASSPATH=".:/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH"
```
* Criar aliases para o Antlr:
```
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
```

* Antlr4-python3-runtime (a versão do pip deve ser a mesma do Antlr)
```
sudo pip install antlr4-python3-runtime==<versão do Antlr instalada>
```

### 2.2  Gerando a gramática
```
antlr4 -Dlanguage=python3 -visitor DND.g4
```

### 2.3 Utilizando a linguagem
```
python3 DND/DNDCompiler.py <arquivo> <pasta de saída>
python3 DND/DNDCompiler.py <arquivo> #irá para uma pasta default chamada result
```


### 2.4 Rodando Casos de Teste
```
chmod +x run
./run
```

