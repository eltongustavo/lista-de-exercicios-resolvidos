valor_inicial_dívida = float(input('Digite o valor inicial da dívida: '))

print('Valor da Dívida...........Valor dos Juros...........Quantidade de Parcelas...........Valor da Parcela')
porcentagem_juros = 0
quantidade_parcelas = 1
for x in range(0, 5):
    valor_dívida_juros = valor_inicial_dívida + (porcentagem_juros / 100 * valor_inicial_dívida)
    print(f"{f'R${valor_dívida_juros:.2f}':26}".replace('.', ','), end='')
    print(f"{f'{porcentagem_juros:2}%':26}{f'{quantidade_parcelas}':33}".replace('.', ','), end='')
    print(f"{f'R${valor_dívida_juros / quantidade_parcelas:.2f}'}".replace('.', ','))
    if porcentagem_juros == 0:
        porcentagem_juros += 10
    else:
        porcentagem_juros += 5

    if quantidade_parcelas == 1:
        quantidade_parcelas += 2
    else:
        quantidade_parcelas += 3
