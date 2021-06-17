import glob, os, codecs, sys


print("========= EXEMPLO 1 =========")

# ----------- LER ARQUIVO TXT -----------
docNormal = ''
filename = 'docs/doc01.txt'
f = codecs.open(filename, 'r', "UTF-8")
for linha in f:
    # remove espaços em branco no inicio e fim de cada linha lida
    docNormal += linha.strip()
f.close()

print(docNormal)
    
# ---------- LER ARQUIVOS PRESENTES EM UM DIRETORIO -------
## fazer importacao no inicio: import glob, os, codecs, sys

print("========= EXEMPLO 2 =========")

for arq in glob.glob("docs/*.txt"):
    print("[{}]".format(arq))
    docTemporario = ''
    
    # Abrir arquivo
    f = codecs.open(arq, "r", "UTF-8")
    linhas = f.readlines()

    for linha in linhas:
        # remove espaços em branco no inicio e fim de cada linha lida
        docTemporario += linha.strip()
    f.close()

    print(docTemporario)
    print()
        
