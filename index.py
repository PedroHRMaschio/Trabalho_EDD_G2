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

    match opcao:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "0":
            break
        case _:
            os.system("cls")
            print("Opção inválida\n")