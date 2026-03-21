grades_list = []
for x in range(0, 4):
    grades_list.append(float(input(f'Digite a nota {x + 1}: ')))

print(f'A média das 4 notas é de {sum(grades_list) / len(grades_list):.1f}')

