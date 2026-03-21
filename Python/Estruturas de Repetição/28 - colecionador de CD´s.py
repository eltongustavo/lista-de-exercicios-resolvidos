quantidade_cds = int(input('Informe quantos cd´s o colecionador comprou: '))
lista_preços_cds = []
for x in range(0, quantidade_cds):
    preço_cd = float(input(f'Informe o preço do cd {x + 1}: '))
    while preço_cd < 0:
        print()
        print('Por favor coloque um preço válido.')
        print()
        preço_cd = float(input(f'Informe o preço do cd {x + 1}: '))
    lista_preços_cds.append(preço_cd)

media_preço_cds = sum(lista_preços_cds) / len(lista_preços_cds)
media_preço_cds_str = f'R${media_preço_cds:.2f}'.replace('.', ',')
print(f'O preço médio por cd que o colecionador comprou foi de {media_preço_cds_str}')
