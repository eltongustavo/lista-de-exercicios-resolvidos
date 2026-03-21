numero = int(input('Digite um número natural: '))
while numero < 0:
    print()
    print('Digite um número natural por favor.')
    print()
    numero = int(input('Digite um número natural: '))

numero_str = numero
contador_divisores = 0

for x in range(numero, 0, -1):
    if numero % x == 0:
        contador_divisores += 1

if contador_divisores > 2:
    print(f'{numero_str} Não é Primo.')
else:
    print(f'{numero_str} é Primo!')


