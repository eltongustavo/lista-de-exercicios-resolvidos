ano = int(input('Digite um ano para descobrir se ele foi ou vai ser bissexto: '))
bissexto = False

decimal_four = float(ano/4) - int(ano/4)
decimal_hundred = float(ano/100) - int(ano/100)
decimal_four_hundred = float(ano/400) - int(ano/400)

if decimal_hundred > 0 and decimal_four_hundred > 0:
    bissexto = True
if decimal_four == 0 and decimal_hundred > 0:
    bissexto = True
if decimal_four == 0 and decimal_hundred == 0 and decimal_four_hundred == 0:
    bissexto = True

if bissexto:
    print(f'{ano} é ou foi um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')
