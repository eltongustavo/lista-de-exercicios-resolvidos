cep_cidades = []
veículos_por_cep = []
quantidade_acidentes = []
cep_acidentes_2000 = []

for x in range(1, 6):
    cep = int(input(f'Digite o cep da cidade {x}: '))
    cep_cidades.append(cep)

    veículos = int(input(f'Quantos veículos existentes atualmente na cidade {x}: '))
    veículos_por_cep.append(veículos)

    acidentes = int(input(f'Quantos acidentes na cidade {x} desde 1999: '))
    if veículos < 2000:
        cep_acidentes_2000.append(acidentes)
    quantidade_acidentes.append(acidentes)
    print()
menor_quantidade_acidentes = quantidade_acidentes[0]
maior_quantidade_acidentes = quantidade_acidentes[0]
cidade_com_mais_acidente = cep_cidades[0]
cidade_com_menos_acidente = cep_cidades[0]

for y, x in enumerate(quantidade_acidentes):
    if x > maior_quantidade_acidentes:
        maior_quantidade_acidentes = x
        cidade_com_mais_acidente = cep_cidades[y]
    elif x < cidade_com_menos_acidente:
        menor_quantidade_acidentes = x
        cidade_com_menos_acidente = cep_cidades[y]

média_quantidade_veículos = sum(veículos_por_cep) / len(veículos_por_cep)
if len(cep_acidentes_2000) == 0:
    média_acidentes_2000 = 0
else:
    média_acidentes_2000 = sum(cep_acidentes_2000) / len(cep_acidentes_2000)
print('='*70)
print(f'Cidade com mais acidentes CEP: {cidade_com_mais_acidente}, Quantidade: {maior_quantidade_acidentes}\n'
      f'\n'
      f'Cidade com menos acidentes CEP: {cidade_com_menos_acidente}, Quantidade: {menor_quantidade_acidentes}\n'
      f'\n'
      f'Média de quantidade de veículos: {média_quantidade_veículos}\n'
      f'\n'
      f'Média de quantidade de veículos nas cidade com menos de 2000 automóveis: {média_acidentes_2000}')






