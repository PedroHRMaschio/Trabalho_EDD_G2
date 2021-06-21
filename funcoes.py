import codecs, pickle, os
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
    arquivo = codecs.open("docs/"+nome_arquivo, "r", "UTF-8")
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

    nome_arquivo = list(nome_arquivo)
    for i in range(0,4):
        nome_arquivo.pop()
    nome_arquivo = "".join(nome_arquivo)
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
    pasta = './docs'
    documentos = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            arquivo = list(arquivo)
            if arquivo[-1] == "l":
                continue
            else:
                arquivo = "".join(arquivo)
                documentos.append(arquivo)
    for documento in documentos:
        funcao_2_aux(documento)
    os.system("cls")
    print("indexação feita com sucesso!\n")

def funcao_3_OR():
    busca = input("\nDigite aqui o que deseja buscar: ")
    busca2 = input("\nDigite aqui a segunda palavra que deseja buscar: ")
    busca = normalize('NFKD', busca)
    busca2 = normalize('NFKD', busca2)
    documentos = []
    nome_documentos_com_palavra = []
    for diretorio, subpastas, arquivos in os.walk("./docs"):
        for arquivo in arquivos:
            arquivo = list(arquivo)
            if arquivo[-1] == "l":
                arquivo = "".join(arquivo)
                documentos.append(arquivo)
    for arquivo in documentos:
        encontrou = False
        f = open("docs/"+arquivo, "rb")
        obj = pickle.load(f)
        for palavra in obj:
            if busca == palavra or busca2 == palavra:
                encontrou = True
        if encontrou:
            arquivo = list(arquivo)
            for i in range(0,12):
                arquivo.pop()
            arquivo = "".join(arquivo)
            nome_documentos_com_palavra.append(arquivo)
    os.system("cls")
    print("Lista do nome dos arquivos com as palavra pricurada:\n")
    print(nome_documentos_com_palavra)


def funcao_3_AND():
    busca = input("\nDigite aqui o que deseja buscar: ")
    busca2 = input("\nDigite aqui a segunda palavra que deseja buscar: ")
    busca = normalize('NFKD', busca)
    busca2 = normalize('NFKD', busca2)
    documentos = []
    nome_documentos_com_palavra = []
    for diretorio, subpastas, arquivos in os.walk("./docs"):
        for arquivo in arquivos:
            arquivo = list(arquivo)
            if arquivo[-1] == "l":
                arquivo = "".join(arquivo)
                documentos.append(arquivo)
    for arquivo in documentos:
        encontrou = False
        encontrou2 = False
        f = open("docs/"+arquivo, "rb")
        obj = pickle.load(f)
        for palavra in obj:
            if busca == palavra:
                encontrou = True
            if busca2 == palavra:
                encontrou2 = True
        if encontrou and encontrou2:
            arquivo = list(arquivo)
            for i in range(0,12):
                arquivo.pop()
            arquivo = "".join(arquivo)
            nome_documentos_com_palavra.append(arquivo)
    os.system("cls")
    print("Lista do nome dos arquivos com as palavra pricurada:\n")
    print(nome_documentos_com_palavra)