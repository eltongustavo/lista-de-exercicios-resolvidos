lista_de_votos = []
contador = 1
while True:
    voto = int(input(f'''Dados os sistemas Operacionais
    1 - Windows Server
    2 - Unix
    3 - Linux
    4 - Netware
    5- Mac OS
    6 - Outro
    \033[31m0 para finalizar a votação\033[m
    
    \033[32m(voto de número {contador})\033[m Qual o melhor deles para gerenciar servidores? '''))

    if voto < 0 or voto > 6:
        print('\033[31m=' * 30)
        print('Valor Inválido')
        print('=' * 30)
        print('\033[m')
    elif voto == 0:
        break
    else:
        lista_de_votos.append(voto)
        contador += 1

print(f'''Windows Server: {lista_de_votos.count(1) * 100 / len(lista_de_votos):.1f}% dos votos - {lista_de_votos.count(1)}
Unix: {lista_de_votos.count(2) * 100 / len(lista_de_votos):.1f}% dos votos - {lista_de_votos.count(2)}
Linux: {lista_de_votos.count(3) * 100 / len(lista_de_votos):.1f}% dos votos - {lista_de_votos.count(3)}
Netware: {lista_de_votos.count(4) * 100 / len(lista_de_votos):.1f}% dos votos - {lista_de_votos.count(4)}
Mac OS: {lista_de_votos.count(5) * 100 / len(lista_de_votos):.1f}% dos votos - {lista_de_votos.count(5)}
Outro Sistema: {lista_de_votos.count(6) * 100 / len(lista_de_votos):.1f}% dos votos - {lista_de_votos.count(6)}''')

sistema_operacional_mais_usado = lista_de_votos.count(0)
for x in range(1, 7):
    if lista_de_votos.count(x) > sistema_operacional_mais_usado:
        sistema_operacional_mais_usado = x
print()
print('=' * 30)
print()
if sistema_operacional_mais_usado == 1:
    print(f'De acordo com a pesquisa, o sistema operacional mais usado em servidores é o Windows Server, com {lista_de_votos.count(1) * 100 / len(lista_de_votos):.1f}% dos votos')
elif sistema_operacional_mais_usado == 2:
    print(f'De acordo com a pesquisa, o sistema operacional mais usado em servidores é o Unix, com {lista_de_votos.count(2) * 100 / len(lista_de_votos):.1f}% dos votos')
elif sistema_operacional_mais_usado == 3:
    print(f'De acordo com a pesquisa, o sistema operacional mais usado em servidores é o Linux, com {lista_de_votos.count(3) * 100 / len(lista_de_votos):.1f}% dos votos')
elif sistema_operacional_mais_usado == 4:
    print(f'De acordo com a pesquisa, o sistema operacional mais usado em servidores é o Netware, com {lista_de_votos.count(4) * 100 / len(lista_de_votos):.1f}% dos votos')
elif sistema_operacional_mais_usado == 5:
    print(f'De acordo com a pesquisa, o sistema operacional mais usado em servidores é o Mac OS, com {lista_de_votos.count(5) * 100 / len(lista_de_votos):.1f}% dos votos')
elif sistema_operacional_mais_usado == 6:
    print(f'De acordo com a pesquisa, o sistema operacional mais usado em servidores é um outro sistema, com {lista_de_votos.count(6) * 100 / len(lista_de_votos):.1f}% dos votos')