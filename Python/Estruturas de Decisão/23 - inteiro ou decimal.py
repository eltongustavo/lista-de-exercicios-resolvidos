num = float(input('Digite um número para saber se ele é inteiro ou decimal: '))
parte_decimal = float(num) - int(num)
if parte_decimal == 0:
    print(f'{int(num)} é Inteiro!')
else:
    print(f'{num} é Decimal!')
