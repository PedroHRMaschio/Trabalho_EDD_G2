import os, funcoes

print("Bem vindo ao programa do trabalho G2 de EDD\n")
print("Acadêmicos: Paulo Santos e Pedro Henrique Ruas Maschio")
print("Professor: Fahad Kalil\n")
while True:
    print("Escolha uma opção:\n")
    print("1: para criar um novo documento")
    print("2: para indexar docuentos presentes na pasta docs")
    print("3: para realizar uma consulta")
    print("0: para sair\n")
    opcao = input("Digite aqui a sua opção: ")

    if opcao == "1":
        funcoes.funcao_1()
    elif opcao == "2":
        funcoes.funcao_2()
    elif opcao == "3":
        os.system("cls")
        print("Como você quer realizar sua pesquisa:\n")
        print("1: Realizar pesquisa usando OR")
        print("2: Realizar usando AND")
        print("0: para voltar ao menu anterior")
        opcao3 = input("\nDigite aqui sua opção: ")
        if opcao3 == "1":
            funcoes.funcao_2()
            funcoes.funcao_3_OR()
        elif opcao3 =="2":
            funcoes.funcao_2()
            funcoes.funcao_3_AND()
        else:
            os.system("cls")
    elif opcao == "0":
        break
    else:
        os.system("cls")
        print("opção inválida!\n")