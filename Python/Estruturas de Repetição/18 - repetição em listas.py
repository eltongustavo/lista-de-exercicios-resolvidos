list_numbers = []
for y in range(0, 5):
    list_numbers.append(int(input('Digite um número: ')))
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


