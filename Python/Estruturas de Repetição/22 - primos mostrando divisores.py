numero = int(input('Digite um número natural: '))
while numero < 0:
    print()
    print('Digite um número natural por favor.')
    print()
    numero = int(input('Digite um número natural: '))

numero_str = numero
lista_divisores = []

for x in range(numero, 0, -1):
    if numero % x == 0:
        lista_divisores.append(x)

if len(lista_divisores) > 2:
    print(f'{numero_str} Não é Primo.\n'
          f'Divisores : {lista_divisores}')

else:
    print(f'{numero_str} é Primo!\n'
          f'Divisores : {lista_divisores}')