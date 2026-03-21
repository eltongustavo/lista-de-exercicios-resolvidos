numero = int(input('Digite de qual número você quer ver a tabuada: '))
inicio = int(input('A partir de qual multiplicador: '))
final = int(input('Até qual multiplicador: '))
if inicio < final:
    for x in range(inicio, final + 1):
        print(f'{numero} x {x} = {numero * x}')
else:
    for x in range(inicio, final - 1, -1):
        print(f'{numero} x {x} = {numero * x}')
