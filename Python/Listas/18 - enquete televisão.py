lista_de_votos = []
while True:
    voto = int(input('Digite o número da camisa do jogador votado: '))
    if voto == 0:
        break

    elif voto < 1 or voto > 23:
        print('\033[31mNúmero Inválido!\033[m')

    else:
        lista_de_votos.append(voto)

print(f'No total foram computados {len(lista_de_votos)} votos')

melhor_jogador = 0

for x in range(1, 24):
    if x in lista_de_votos:
        print(f'\033[32m{lista_de_votos.count(x)} votos\033[m no Camisa {x}')
    if lista_de_votos.count(x) > melhor_jogador:
        melhor_jogador = x

for x in range(1, 24):
    quant_votos = lista_de_votos.count(x)
    if quant_votos == 0:
        break
    else:
        print(f'O percentual de voto do Camisa {x} foi de \033[32m{quant_votos * 100 / len(lista_de_votos):1f}%\033[m')

print(f'O melhor jogador foi o Camisa {melhor_jogador}, com \033[32m{lista_de_votos.count(melhor_jogador) * 100 / len(lista_de_votos):.1f}% dos votos\033[m')







