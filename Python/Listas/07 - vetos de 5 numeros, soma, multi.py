numbers_list = []
for x in range(0, 5):
    numbers_list.append(float(input('Digite um número: ')))

sum_numbers = sum(numbers_list)
multi_numbers = 1
for x in numbers_list:
    multi_numbers *= x

print('Os números digitados foram: ')
for x in numbers_list:
    print(x, end=' ')
print()

print('=' * 40)

print(f'A soma dos números é de {sum_numbers}')

print('=' * 40)

print(f'A multiplicação dos números foi de {multi_numbers}')
