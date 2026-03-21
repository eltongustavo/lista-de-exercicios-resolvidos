nome = input("Digite seu nome: ")
for x in range(len(nome), 0, -1):
    print(nome[0:x].upper())