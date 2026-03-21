print('Validador de datas')
validação_dia = validação_mes = validação_ano = True
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if dia < 0 or dia > 31:
    validação_dia = False
if mes < 0 or mes > 12:
    validação_mes = False
if ano < 0:
    validação_ano = False

if validação_dia and validação_mes and validação_ano:
    print(f'{dia}/{mes}/{ano} é uma data válida!')
else:
    print(f'{dia}/{mes}/{ano} não é uma data válida!')