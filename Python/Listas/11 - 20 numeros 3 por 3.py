numbers_list_one = []
for _ in range(0, 10):
    numbers_list_one.append(float(input('Digite um número da lista um: ')))

numbers_list_two = []
for _ in range(0, 10):
    numbers_list_two.append(float(input('Digite um número da lista dois: ')))

numbers_list_junction = []

start = 0
end = 3

aux_one = []
aux_two = []
while end <= 11:
    for x, _ in enumerate(range(start, end)):
        aux_one.append(numbers_list_one[start:end])
        numbers_list_junction.append(aux_one[x])

        aux_two.append(numbers_list_two[start:end])
        numbers_list_junction.append(aux_two[x])
        start += 3
        end += 3

print(numbers_list_junction)




