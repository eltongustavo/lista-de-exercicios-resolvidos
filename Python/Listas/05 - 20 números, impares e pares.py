numbers_list = []
even_numbers = []
odd_numbers = []
for x in range(0, 20):
    numbers_list.append(float(input('Digite um número: ')))

for y in numbers_list:
    if y % 2 == 0:
        even_numbers.append(y)
    else:
        odd_numbers.append(y)


print(f'Todos os números: ')
for number in numbers_list:
    print(number, end=' / ')

print(f'Os números pares: ')
for even in even_numbers:
    print(even, end=' / ')

print(f'Os números ímpares: ')
for odd in odd_numbers:
    print(odd, end=' / ')