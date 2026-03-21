cachorro_quente = bauru_simples = bauru_com_ovo = hamburguer = cheeseburguer = refrigerante = 0
while True:
    print('''Especificação      Código     Preço
Cachorro Quente    100        R$ 1,20
Bauru Simples      101        R$ 1,30
Bauru com ovo      102        R$ 1,50
Hambúrguer         103        R$ 1,20
Cheeseburguer      104        R$ 1,30
Refrigerante       105        R$ 1,00''')
    print()

    codigo = int(input('De acordo com a tabela acima\n'
                       'Qual o codigo do produto que quer adicionar ao carrinho? (qualquer codigo diferente'
                       ' encerra os pedidos): '))
    print()
    if codigo < 100 or codigo > 105:
        break

    else:
        quantidade = int(input(f'Digite qual quantidade do produto de cod({codigo}) será comprada: '))
        if quantidade <= 0:
            print('Quantidade inválida, o programa será reininciado!')
            print('=' * 60)
            continue

        else:
            print()
            print(f'\033[32m{quantidade} unidades do produto de cod({codigo}) adicionados ao carrinho com sucesso.\033[m')
            print()

            if codigo == 100:
                cachorro_quente += quantidade

            elif codigo == 101:
                bauru_simples += quantidade

            elif codigo == 102:
                bauru_com_ovo += quantidade

            elif codigo == 103:
                hamburguer += quantidade

            elif codigo == 104:
                cheeseburguer += quantidade

            elif codigo == 105:
                refrigerante += quantidade

            proximo_pedido = str(input('Quer fazer mais algum pedido? (S/N): ')).upper()[0]
            while proximo_pedido not in 'SN':
                proximo_pedido = str(input('Quer fazer mais algum pedido? (S/N): ')).upper()[0]
            if proximo_pedido == 'N':
                break
            else:
                print()
                continue

if cachorro_quente == 0:
    print('', end='')
elif cachorro_quente == 1:
    print(f'{f"{cachorro_quente} cachorro quente":40}R${cachorro_quente * 1.20:.2f}'.replace('.', ','))
else:
    print(f'{f"{cachorro_quente} cachorros quentes":40}R${cachorro_quente * 1.20:.2f}'.replace('.', ','))


if bauru_simples == 0:
    print('', end='')
elif bauru_simples == 1:
    print(f'{f"{bauru_simples} bauru simples":40}R${bauru_simples * 1.30:.2f}'.replace('.', ','))
else:
    print(f'{f"{bauru_simples} baurus simples":40}R${bauru_simples * 1.30:.2f}'.replace('.', ','))


if bauru_com_ovo == 0:
    print('', end='')
elif bauru_com_ovo == 1:
    print(f'{f"{bauru_com_ovo} bauru com ovo":40}R${bauru_com_ovo * 1.50:.2f}'.replace('.', ','))
else:
    print(f'{f"{bauru_com_ovo} baurus com ovo":40}R${bauru_com_ovo * 1.50:.2f}'.replace('.', ','))


if hamburguer == 0:
    print('', end='')
elif hamburguer == 1:
    print(f'{f"{hamburguer} hamburguer":40}R${hamburguer * 1.20:.2f}'.replace('.', ','))
else:
    print(f'{f"{hamburguer} hamburguers":40}R${hamburguer * 1.20:.2f}'.replace('.', ','))


if cheeseburguer == 0:
    print('', end='')
elif cheeseburguer == 1:
    print(f'{f"{cheeseburguer} cheeseburguer":40}R${cheeseburguer * 1.30:.2f}'.replace('.', ','))
else:
    print(f'{f"{cheeseburguer} cheeseburguers":40}R${cheeseburguer * 1.30:.2f}'.replace('.', ','))


if refrigerante == 0:
    print('', end='')
elif refrigerante == 1:
    print(f'{f"{refrigerante} refrigerante":40}R${refrigerante * 1.00:.2f}'.replace('.', ','))
else:
    print(f'{f"{refrigerante} refrigerantes":40}R${refrigerante * 1.00:.2f}'.replace('.', ','))


soma_pedidos = (cachorro_quente * 1.20) + (bauru_simples * 1.30) + \
               (bauru_com_ovo * 1.50) + (hamburguer * 1.20) + (cheeseburguer * 1.30) + (refrigerante * 1.00)
print('-' * 50)
print(f'{f"Soma de Preços":40}R${soma_pedidos:.2f}'.replace('.', ','))
