import codecs, pickle
from unicodedata import normalize

def funcao_2_aux(nome_arquivo):

    #criar um array com as pontuações para remover pontuação depois
    pontuacao = []
    arqpontuacao = codecs.open("test/pontuacao.txt", "r", "UTF-8")
    linhas = arqpontuacao.readlines()
    for linha in linhas:
        pontuacao.append(linha.replace('\n', '').strip().lower())
    arqpontuacao.close()

    #criar um array com stopwords para remover depois
    stopwords = []
    arq = codecs.open("test/stopwords.txt", "r", "UTF-8")
    linhas = arq.readlines()
    for linha in linhas:
        stopwords.append(linha.replace('\n', '').strip().lower())
    arq.close()

    #realizar tokenização
    arquivo = codecs.open("docs/"+nome_arquivo+".txt", "r", "UTF-8")
    linhas_arquivo = arquivo.readlines()
    palavras = []
    for linha in linhas_arquivo:
        for palavra in linha.split(" "):
            palavras.append(palavra.replace('\n', '').strip().lower())
    arquivo.close()

    #remover stopwords
    apos_remover_stopwords = []
    for p in palavras:
        if (p.upper() in stopwords) or (p.lower() in stopwords):
            continue
        else:
            apos_remover_stopwords.append(p)

    #remover pontuação e acentos
    apos_remover_pontuacao = []
    for p in apos_remover_stopwords:
        if "".__eq__(p):
            continue
        else:
            p = normalize('NFKD', p).encode('ASCII','ignore').decode('ASCII')
            for letra in p:
                if (letra in pontuacao):
                    p = list(p)
                    p.remove(letra)
                    p = "".join(p)
                else:
                    continue
            apos_remover_pontuacao.append(p)

    #Realizando o salvamento do objeto com a biblioteca pickle
    arquivo = open("docs/"+nome_arquivo+"_pickle.pckl", "wb")
    arquivo.write(pickle.dumps(apos_remover_pontuacao))
    arquivo.close()


def funcao_1():
    documento = input("Digite aqui o nome do seu documento: ")
    arquivo = open("docs/"+documento+".txt", "w")
    escrita = input("\nDigite aqui o que você deseja colocar no seu documento: ")
    arquivo.write(escrita)


def funcao_2():
    pass