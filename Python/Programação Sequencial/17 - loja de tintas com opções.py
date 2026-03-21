area = int(input('Informe quantos metros serão pintados: '))
area = area * 1.1
excesso = area - int(area)
area = int(area)
if excesso > 0:
    area += 1

litros = area // 6
if area % 6 > 0:
    litros += 1
litros_aux = litros
print('-='*30)
print(f'Para pintar a área de {area}m², serão necessários {litros} litros.')
print('-='*30)
#----------------------------------------------------------------
quant_latas = 0
while litros_aux > 18:
    quant_latas += 1
    litros_aux -= 18
if litros_aux > 0:
    quant_latas += 1
preco_latas = f'{quant_latas * 80:.2f}'.replace('.', ',')

print(f'\033[32mOpção 1) Comprar {quant_latas} latas de 18L: R${preco_latas}\033[m')
print()
#----------------------------------------------------------------
litros_aux = litros

quant_gal = 0
while litros_aux > 3.6:
    quant_gal += 1
    litros_aux -= 3.6
if litros_aux > 0:
    quant_gal += 1
preco_gal = f'{quant_gal * 25:.2f}'.replace('.', ',')
print(f'\033[32mOpção 2) Comprar {quant_gal} galões de 3.6L: R${preco_gal}\033[m')
print()

litros_aux = litros

quant_latas = litros_aux // 18

resto_litros = litros_aux % 18

quant_gal = resto_litros // 3.6
if resto_litros % 3.6 > 0:
    quant_gal += 1
if quant_gal > 3:
    quant_gal = 0
    quant_latas += 1
valor = f'{(quant_latas * 80) + (quant_gal * 25):.2f}'.replace('.', ',')
print(f'\033[32mOpção 3) Comprar {quant_latas} latas de 18L e {int(quant_gal)} galões de 3.6L, visando maior economia, totalizando R${valor}\033[m')
print()

litros_aux = litros

quant_latas = litros_aux // 18
resto_litros = litros_aux % 18
quant_gal = resto_litros // 3.6
if resto_litros % 3.6 > 0:
    quant_gal += 1
valor = f'{(quant_latas * 80) + (quant_gal * 25):.2f}'.replace('.', ',')
print(f'\033[32mOpção 4) Comprar {quant_latas} latas de 18L e {int(quant_gal)} galões de 3.6L, visando menor desperdício de litros, totalizando R${valor}\033[m')









