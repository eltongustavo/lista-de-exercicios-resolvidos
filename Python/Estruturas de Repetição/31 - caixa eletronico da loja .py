from time import sleep

lista_preço_produtos = []
contador = 1
while True:
    preço_produto = float(input(f'Digite o preço do produto {contador}   (0 para finalizar): \033[32mR$\033[m'))
    if preço_produto < 0:
        print('\033[31mPreço Inválido, o programa será reiniciado.\033[m')
        contador = 1
        continue
    else:
        contador += 1
        lista_preço_produtos.append(preço_produto)
        if preço_produto == 0:
            print('=' * 60)
            print(f'Todos os {contador - 2} produtos foram adicionados ao carrinho. ')
            print(f'O preço total dos produtos é de \033[32mR${sum(lista_preço_produtos):.2f}\033[m'.replace('.', ','))
            print('=' * 60)
            pagamento = float(input('Digite o valor em dinheiro que o cliente irá pagar: '))
            print('=' * 60)

            if pagamento == sum(lista_preço_produtos):
                print('O troco é de \033[32mR$00,00\033[m')

            elif pagamento > sum(lista_preço_produtos):
                troco = pagamento - sum(lista_preço_produtos)
                print(f'O troco é de \033[32mR${troco:.2f}\033[m')

            elif sum(lista_preço_produtos) > pagamento:
                troco = sum(lista_preço_produtos) - pagamento
                print(f'Faltam \033[32mR${troco:.2f}\033[m para completar o pagamento.')

            contador = 1
            print('=' * 60)
            print('O programa será reininciado em \033[33m', end='')
            for x in range(10, 0, -1):
                print(f'\033[33m{x}\033[m', flush=False, end=' ')
                sleep(1)
            lista_preço_produtos.clear()
            print()