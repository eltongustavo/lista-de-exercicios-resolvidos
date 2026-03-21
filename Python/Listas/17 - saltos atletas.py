while True:
    atleta = str(input('Digite o nome do atleta: ')).strip()
    if atleta == '':
        print('Programa Encerrado.')
        break

    lista_de_saltos = []
    for x in range(0, 5):
        salto = float(input(f'De quantos metros foi o salto {x + 1}: '))
        lista_de_saltos.append(salto)

    print(f'''Nome do Atleta: {atleta}
Saltos:''')
    for x in lista_de_saltos:
        print(f'{x:.1f}m', end='')
        if lista_de_saltos.index(x) == 4:
            print('')
        else:
            print(' - ', end='')

    print(f'Média de saltos : {sum(lista_de_saltos) / len(lista_de_saltos):.1f}m')
    lista_de_saltos.clear()






