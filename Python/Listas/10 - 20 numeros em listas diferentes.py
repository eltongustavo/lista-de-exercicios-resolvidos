numbers_list_one = []
for _ in range(0, 10):
    numbers_list_one.append(float(input('Digite um número da lista um: ')))

numbers_list_two = []
for _ in range(0, 10):
    numbers_list_two.append(float(input('Digite um número da lista dois: ')))

numbers_list_junction = []

for y, x in enumerate(numbers_list_one):
    numbers_list_junction.append(x)
    numbers_list_junction.append(numbers_list_two[y])

print(numbers_list_junction)
