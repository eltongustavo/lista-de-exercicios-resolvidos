numbers_list = []
for _ in range(0, 10):
    numbers_list.append(float(input('Digite um número: ')))
print()
print('A sequência de 10 números inversos é: ')

print(numbers_list[::-1])
