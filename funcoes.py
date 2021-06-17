import codecs

def stopwords_def(nome_arquivo):

    stopwords = []
    arq = codecs.open("test/stopwords.txt", "r", "UTF-8")
    linhas = arq.readlines()
    for linha in linhas:
        stopwords.append(linha.replace('\n', '').strip().lower())
    arq.close()

    arquivo = codecs.open(nome_arquivo, "r", "UTF-8")
    linhas_arquivo = arquivo.readlines()
    palavras = []
    for linha in linhas_arquivo:
        for palavra in linha.split(" "):
            palavras.append(palavra.replace('\n', '').strip().lower())
    arquivo.close()

    apos_remover_stopwords = []
    for p in palavras:
        if (p.upper() in stopwords) or (p.lower() in stopwords):
            continue
        else:
            apos_remover_stopwords.append(p)
    
    return apos_remover_stopwords

def funcao_1():
    documento = input("Digite aqui o nome do seu documento: ")
    arquivo = open("docs/"+documento+".txt", "w")
    escrita = input("\nDigite aqui o que você deseja colocar no seu documento: ")
    arquivo.write(escrita)

def funcao_2():
    pass