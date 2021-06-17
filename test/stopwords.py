import codecs

stopwords = []
nome_arq = 'test/stopwords.txt'

arq = codecs.open(nome_arq, "r", "UTF-8")
linhas = arq.readlines()
for linha in linhas:    
    stopwords.append(linha.replace('\n', '').strip().lower())
arq.close()

## -- TESTES --

texto_doc1 = "Se no Rio de Janeiro não houvessem crimes, seria ótimo"
print("Texto Original: {}".format(texto_doc1))
apos_remover_stopwords = []

for p in texto_doc1.split(" "):    
    if (p.upper() in stopwords) or (p.lower() in stopwords):
        print("> Stopword '{}' encontrada <".format(p))
        continue
    else:
        apos_remover_stopwords.append(p)

print("Novo Texto: {}".format(apos_remover_stopwords))
