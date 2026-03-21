numbers_list = []
for _ in range(0, 9):
    numbers_list.append(float(input('Digite um número: ')))

sum_square = 0
for x in numbers_list:
    sum_square += (x ** 2)

print(f'A soma dos quadrados dos números lidos é de {sum_square}')




