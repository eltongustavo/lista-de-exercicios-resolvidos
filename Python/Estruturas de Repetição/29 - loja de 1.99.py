preço_inicial = 1.99
print('Loja Quase Dois - Tabela de Preços:')
print('-'*15)
for x in range(1, 51):
    print(f'{x:2} - R${preço_inicial * x:.2f}'.replace('.', ','))
print('-'*15)