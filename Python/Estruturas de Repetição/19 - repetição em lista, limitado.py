list_numbers = []

while len(list_numbers) < 5:
    
    number = int(input('Digite um número: '))

    if 0 < number < 1000:
        print()
        print(f'{number} adicionado com sucesso.')
        print()
        list_numbers.append(number)

    else:
        print()
        print('Digite um número entre 0 e 1000 por gentileza.')
        print()

maior = list_numbers[0]
menor = list_numbers[0]
soma = 0

for x in list_numbers:
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    soma += x

print(f'O maior valor da lista é {maior}\n'
      f'O menor valor da lista é {menor}\n'
      f'A soma dos valores da lista é {soma}')