lista_carros = ['a', 'b', 'c', 'd', 'e']
km_litro = [8, 9, 10, 8.5, 6]

print(f'Dentro as opções de carro, o mais econômico é o carro {lista_carros[km_litro.index(max(km_litro))]}')
print()
for y, x in enumerate(km_litro):
    print(f'Para percorrer 1000km, o carro {y} irá gastar pelo menos \033[33m{1000//x}L\033[m de gasolina, totalizando \033[32mR${1000 // x * 2.25:.2f}\033[m')
