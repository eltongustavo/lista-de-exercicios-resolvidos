from time import sleep
jumps_distance_list = []
counter = 1
while True:
    name_athlete = str(input(f'Qual o nome do atleta {counter}: ')).title()
    if name_athlete == '' or name_athlete == ' ':
        print('Programa encerrando...')
        sleep(2)
        exit()
    else:
        for x in range(1, 6):
            jump = float(input(f'Qual a distância do salto {x} (em metros): '))
            jumps_distance_list.append(jump)
        jumps_distance_list.sort(reverse=True)

        best_jump = jumps_distance_list[0]
        worst_jump = jumps_distance_list[4]

        avarege_three_jumps = sum(jumps_distance_list[1:4]) / 3

        print()

        print(f'Atleta : {name_athlete}')

        print()

        print('-' * 50)

        print('Saltos em ordem decrescente:')

        for y, x in enumerate(jumps_distance_list):
            print(f'{y + 1}º salto: {x}m')
        print('-' * 50)

        print()

        print(f'''Melhor salto: {best_jump}m
Pior salto: {worst_jump}m
Média dos demais saltos: {avarege_three_jumps}m''')

        print()

        print(f'Resultado final:\n'
              f'{name_athlete} : {avarege_three_jumps}m')

        print()

        print('=' * 50)
        counter += 1
        jumps_distance_list.clear()
