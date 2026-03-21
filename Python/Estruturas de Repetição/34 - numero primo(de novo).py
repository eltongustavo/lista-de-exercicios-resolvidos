numero = int(input('Digite um número natural: '))
while numero < 0:
    print()
    print('\033[31mDigite um número natural por favor.\033[m')
    print()
    numero = int(input('Digite um número natural: '))

contador_divisores = 0

for x in range(numero, 0, -1):
    if numero % x == 0:
        contador_divisores += 1

if contador_divisores > 2:
    print(f'{numero} \033[31mNão é\033[m Primo.')
else:
    print(f'{numero} \033[32mé\033[m Primo!')
