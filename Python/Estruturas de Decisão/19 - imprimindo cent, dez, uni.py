num = int(input('Digite um número menor que 1000: '))
if num >= 1000:
    print('Número Inválido')
    exit()

centenas_str = dezenas_str = unidades_str = ''
if num >= 100:
    centanas_int = num // 100
    resto = num % 100
    if centanas_int == 0:
        centenas_str = ''
    else:
        if centanas_int == 1:
            centenas_str = '1 centena'
        else:
            centenas_str = f'{centanas_int} centenas'

resto_centenas_aux = num % 100

if resto_centenas_aux >= 10:
    dezenas_int = resto_centenas_aux // 10
    if dezenas_int == 1:
        dezenas_str = '1 dezena'
    elif dezenas_int == 0:
        dezenas_str = ''
    else:
        dezenas_str = f'{dezenas_int} dezenas'

resto_dezenas_aux = resto_centenas_aux % 10

if resto_dezenas_aux > 0:
    unidade_int = resto_dezenas_aux // 1
    if unidade_int == 1:
        unidades_str = '1 unidade'
    elif unidade_int == 0:
        unidades_str = ''
    else:
        unidades_str = (f'{unidade_int} unidades')

resto_unidade_aux = resto_dezenas_aux % 1

print(centenas_str, end='')
if resto_centenas_aux > 10 and unidades_str != '' and centenas_str != '':
    print(', ', end='')
elif dezenas_str == unidades_str == '':
    print('')
else:
    if centenas_str != '':
        print(' e ', end='')

print(dezenas_str, end='')
if resto_dezenas_aux >= 1:
    if dezenas_str != '':
        print(' e ', end='')

print(unidades_str)




