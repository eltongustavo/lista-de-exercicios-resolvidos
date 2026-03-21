produto_1 = float(input('Digite o preço do produto 1: '))
produto_2 = float(input('Digite o preço do produto 2: '))
produto_3 = float(input('Digite o preço do produto 3: '))

mais_barato = produto_1
num_produto = 1
if produto_2 < mais_barato:
    mais_barato = produto_2
    num_produto = 2
if produto_3 < mais_barato:
    mais_barato = produto_3
    num_produto = 3
print(f'''Produto 1: {produto_1:.2f}
Produto 2: {produto_2:.2f}
Produto 3: {produto_3:.2f}
Julius decidiu levar o \033[32mproduto de número {num_produto}\033[m, que custa \033[32mR${mais_barato:.2f}\033[m''')