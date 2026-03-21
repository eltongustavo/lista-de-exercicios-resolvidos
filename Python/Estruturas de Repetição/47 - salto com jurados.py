grades_list = []
counter = 1
while True:
    name_athlete = input(f'Qual o nome do atleta de número {counter}: ').title()

    for x in range(1, 8):
        jury_vote = float(input(f'Qual o voto do jurado {x}: '))
        grades_list.append(jury_vote)
    grades_list_aux = grades_list[:]
    grades_list.sort(reverse=True)

    best_grade = grades_list[0]
    worst_grade = grades_list[6]
    avarege_five_grades = sum(grades_list[1:6]) / 5

    print('=' * 50)
    print(f'Atleta: {name_athlete}')
    print()
    for y, x in enumerate(grades_list_aux):
        print(f'Nota do Jurado {y + 1}: \033[32m{x}\033[m')

    print('=' * 50)
    print()
    print(f'''Resultado Final: 
Atleta : {name_athlete}
Melhor Nota : {best_grade:.1f}
Pior Nota : {worst_grade:.1f}
Média : {avarege_five_grades:.1f}''')
    print()
    print('=' * 50)
    print()
    counter += 1
    grades_list.clear()


