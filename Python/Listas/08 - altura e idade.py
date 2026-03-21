lists_len_age = []
for x in range(1, 6):
    len_person = float(input(f'Digite a altura da pessoa {x}: '))
    age_person = int(input(f'Digite a idade da pessoa {x}: '))
    print()
    aux = [len_person, age_person]
    lists_len_age.append(aux)

for x in range(5, 0, -1):
    print('=' * 50)
    print(f'A altura da pessoa {x} é de \033[32m{lists_len_age[x - 1][0]:.2f}m\033[m')
    print(f'A idade da pessoa {x} é de \033[32m{lists_len_age[x - 1][1]} anos\033[m')
    print('=' * 50)



