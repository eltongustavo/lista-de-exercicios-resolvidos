grades_list = []
condição = True
while condição:
    grade = float(input('Digite a nota: (-1 para finalizar) '))
    if grade == -1:
        condição = False
    else:
        grades_list.append(grade)

print(f'A quantidade de notas armazenadas foi de {len(grades_list)}')
for x in grades_list:
    print(x, end=' ')
print()

for x in grades_list[::-1]:
    print(x)
print()

print(f'A soma de todos os valores é de {sum(grades_list)}')
print(f'A média de todos os valores é de {sum(grades_list) / len(grades_list)}')

numbers_higher_than_average = 0
for x in grades_list:
    if x > (sum(grades_list) / len(grades_list)):
        numbers_higher_than_average += 1

print(f'Existem {numbers_higher_than_average} valores acima da média na lista.')

numbers_less_than_seven = 0
for x in grades_list:
    if x < 7:
        numbers_less_than_seven += 1

print(f'Existem {numbers_less_than_seven} números menores que sete nessa lista.')

print('THE END!')



