num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite outro número: '))

op = input('''Digite qual das opções abaixo você quer realizar:
1) Par ou Impar
2) Positivo, Negativo ou Nulo
3) Inteiro ou Decimal
: ''')

if op == '1':
    print('Eis o resultado da opção escolhida:')
    print()

    resto_1 = num_1 % 2
    resto_2 = num_2 % 2

    if resto_1 == 0:
        print(f'{num_1} é Par!')
    else:
        print(f'{num_1} é Impar!')
    if resto_2 == 0:
        print(f'{num_2} é Par!')
    else:
        print(f'{num_2} é Impar!')

elif op == '2':
    print('Eis o resultado da opção escolhida:')
    print()

    if num_1 > 0:
        print(f'{num_1} é Positivo!')
    elif num_1 == 0:
        print(f'{num_1} é Nulo!')
    else:
        print(f'{num_1} é Negativo!')

    if num_2 > 0:
        print(f'{num_2} é Positivo!')
    elif num_2 == 0:
        print(f'{num_2} é Nulo!')
    else:
        print(f'{num_2} é Negativo!')

elif op == '3':
    print('Eis o resultado da opção escolhida:')
    print()

    decimal_num_1 = float(num_1) - int(num_1)
    decimal_num_2 = float(num_2) - int(num_2)

    if decimal_num_1 == 0:
        print(f'{int(num_1)} é Inteiro!')
    else:
        print(f'{num_1} é Decimal!')

    if decimal_num_2 == 0:
        print(f'{int(num_2)} é Inteiro!')
    else:
        print(f'{num_2} é Decimal!')
else:
    print('Opção Inválida!')


