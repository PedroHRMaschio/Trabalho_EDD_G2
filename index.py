import os, funcoes

print("Bem vindo ao programa do trabalho G2 de EDD\n")
print("Acadêmicos: Paulo Santos e Pedro Henrique Ruas Maschio")
print("Professor: Fahad Kalil\n")
while True:
    print("Escolha uma opção:\n")
    print("1: para criar um novo documento")
    print("2: para indexar docuentos presentes na pasta docs")
    print("3: para realizar uma consulta")
    print("4: para mostrar índice invertido")
    print("0: para sair\n")
    opcao = input("Digite aqui a sua opção: ")

    if opcao == "1":
        funcoes.funcao_1()
    elif opcao == "2":
        pass
    elif opcao == "3":
        os.system("cls")
        print("Como você quer realizar sua pesquisa:\n")
        print("1: Realizar pesquisa usando OR")
        print("2: Realizar usando AND")
        print("0: para voltar ao menu anterior")
        opcao3 = input("\nDigite aqui sua opção: ")
        if opcao3 == "1":
            pass
        elif opcao3 =="2":
            pass
        else:
            pass
    elif opcao == "4":
        pass
    elif opcao == "0":
        break
    else:
        os.system("cls")
        print("opção inválida!\n")