preçoL_até_20_alcool = 1.90 - (3 / 100 * 1.90)
preçoL_acima_20_alcool = 1.90 - (5 / 100 * 1.90)

preçoL_até_20_gasolina = 2.50 - (4 / 100 * 2.50)
preçoL_acima_20_gasolina = 2.50 - (6 / 100 * 2.50)

litros = int(input('Digite quantos litros você quer colocar: '))
tipo_compustível = input('Digite o tipo de combustível que seu carro usa: (A-Alcool, G-Gasolina): ').upper()[0]
while tipo_compustível not in 'AG':
    print()
    print('Por favor escolha entre as opções na pergunta.')
    print()
    tipo_compustível = input('Digite o tipo de combustível que seu carro usa: (A-Alcool, G-Gasolina): ').upper()[0]

if tipo_compustível == 'A':
    if litros <= 20:
        preço = f'R${litros * preçoL_até_20_alcool:.2f}'.replace('.', ',')
        print(f'Você escolheu comprar {litros}L do combustível Alcool, terá um desconto de 3% por litro, totalizando {preço}')

    elif litros > 20:
        preço = f'R${litros * preçoL_acima_20_alcool:.2f}'.replace('.', ',')
        print(f'Você escolheu comprar {litros}L do combustível Alcool, terá um desconto de 5% por litro, totalizando {preço}')

elif tipo_compustível == 'G':
    if litros <= 20:
        preço = f'R${litros * preçoL_até_20_gasolina:.2f}'.replace('.', ',')
        print(f'Você escolheu comprar {litros}L do combustível Gasolina, terá um desconto de 4% por litro, totalizando {preço}')
    elif litros > 20:
        preço = f'R${litros * preçoL_acima_20_gasolina:.2f}'.replace('.', ',')
        print(f'Você escolheu comprar {litros}L do combustível Gasolina, terá um desconto de 6% por litro, totalizando {preço}')

