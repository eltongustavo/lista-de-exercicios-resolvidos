from random import randint

lista_lados = [0, 0, 0, 0, 0, 0]

for x in range(0, 100):
    jogada = randint(1, 6)

    if jogada == 1:
        lista_lados[0] += 1

    elif jogada == 2:
        lista_lados[1] += 1

    elif jogada == 3:
        lista_lados[2] += 1

    elif jogada == 4:
        lista_lados[3] += 1

    elif jogada == 5:
        lista_lados[4] += 1

    elif jogada == 6:
        lista_lados[5] += 1

for y, x in enumerate(lista_lados):
    print(f'O lado {y + 1} foi tirado um total de {x} vezes')

