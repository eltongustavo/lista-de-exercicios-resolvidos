area_pintada = int(input('Digite a área a ser pintada em metros²: '))
litros = (area_pintada // 3)
if area_pintada % 3 > 0:
    litros += 1
latas_compradas = litros // 18
if litros % 18 > 0:
    latas_compradas += 1
valor_latas = 80.00 * latas_compradas
print(f'De acordo a área de {area_pintada}m², serão necessárias {latas_compradas} latas, com um preço de {valor_latas}R$')

