def ValorFatura():
    continuar = True
    lista_pagamentos = []
    while continuar:
        divida = float(input('Digite o valor da dívida: R$'))
        dias_em_atraso = int(input('Quantos dias está em atraso? '))
        if dias_em_atraso == 0:
            dívida_com_juros = divida + (3 * 100 / divida)
        else:
            dívida_com_juros = divida + (3 * 100 / divida) + ((1 / 100 * divida) * dias_em_atraso)

        lista_pagamentos.append(dívida_com_juros)

        next_quest = input('Você quer Continuar? S/N ').upper()[0]
        while next_quest not in 'SN':
            next_quest = input('Você quer Continuar? S/N ').upper()[0]
        if next_quest == 'S':
            continue
        if next_quest == 'N':
            continuar = False
        for y, x in enumerate(lista_pagamentos):
            print(f'Valor da dívida {y+1} = R${x:.2f}')

ValorFatura()


