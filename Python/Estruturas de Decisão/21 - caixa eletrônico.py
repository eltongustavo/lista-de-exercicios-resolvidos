notas_100 = notas_50 = notas_20 = notas_10 = notas_5 = notas_2 = moeda_1 = 0
saque = int(input('Digite a quantia em R$ do saque: R$'))
if saque < 10 or saque > 600:
    print('Valor inválido, Digite um Valor entre R$10,00 e R$600,00')
    exit()
else:
    print(f'Para receber o valor de \033[32mR${saque}\033[m, o banco lhe dará ', end='')

    notas_100 = saque // 100
    saque = saque % 100
    if notas_100 > 0:
        if notas_100 == 1:
            print('\033[33m1 nota\033[m de \033[32mR$100\033[m', end='')
        else:
            print(f'\033[33m{notas_100} notas\033[m de \033[32mR$100\033[m', end='')

    notas_50 = saque // 50
    saque = saque % 50
    if notas_50 == 0:
        print('', end='')
    else:
        if saque != 0:
            print(', ', end='')
        else:
            print(' e ', end='')
        if notas_50 == 1:
            print('\033[33m1 nota\033[m de \033[32mR$50\033[m', end='')
        else:
            print(f'\033[33m{notas_50} notas\033[m de \033[32mR$50\033[m', end='')


    notas_20 = saque // 20
    saque = saque % 20
    if notas_20 == 0:
        print('', end='')
    else:
        if saque != 0:
            print(', ', end='')
        else:
            print(' e ', end='')
        if notas_20 == 1:
            print('\033[33m1 nota\033[m de \033[32mR$20\033[m', end='')
        else:
            print(f'\033[33m{notas_20} notas\033[m de \033[32mR$20\033[m', end='')

    notas_10 = saque // 10
    saque = saque % 10
    if notas_10 == 0:
        print('', end='')
    else:
        if saque != 0:
            print(', ', end='')
        else:
            print(' e ', end='')
        if notas_10 == 1:
            print('\033[33m1 nota\033[m de \033[32mR$10\033[m', end='')
        else:
            print(f'\033[33m{notas_10} notas\033[m de \033[32mR$10\033[m', end='')

    notas_5 = saque // 5
    saque = saque % 5
    if notas_5 == 0:
        print('', end='')
    else:
        if saque != 0:
            print(', ', end='')
        else:
            print(' e ', end='')
        if notas_5 == 1:
            print('\033[33m1 nota\033[m de \033[32mR$5\033[m', end='')
        else:
            print(f'\033[33m{notas_5} notas\033[m de \033[32mR$5\033[m', end='')

    notas_2 = saque // 2
    saque = saque % 2
    if notas_2 == 0:
        print('', end='')
    else:
        if saque != 0:
            print(', ', end='')
        else:
            print(' e ', end='')
        if notas_2 == 1:
            print('\033[33m1 nota\033[m de \033[32mR$2\033[m', end='')
        else:
            print(f'\033[33m{notas_2} notas\033[m de \033[32mR$2\033[m', end='')

    moeda_1 = saque // 1
    saque = saque % 1
    if moeda_1 == 0:
        print('', end='')
    else:
        if saque != 0:
            print(', ', end='')
        else:
            print(' e ', end='')
        if moeda_1 == 1:
            print('\033[33m1 moeda\033[m de \033[32mR$1\033[m', end='')
        else:
            print(f'\033[33m{moeda_1}\033[m moedas de \033[32mR$1\033[m', end='')



