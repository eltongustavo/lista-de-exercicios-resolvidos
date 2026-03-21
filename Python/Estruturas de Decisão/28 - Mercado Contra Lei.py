tipo_carne = input('''F - File Duplo
A - Alcanha
P - Picanha
Digite qual tipo de carne o cliente irá levar: ''').upper()[0]
while tipo_carne not in 'FAP':
    print()
    print('Por favor escolha uma das opções abaixo!')
    print()
    tipo_carne = input('''F - File Duplo
A - Alcanha
P - Picanha
Digite qual tipo de carne o cliente irá levar: ''').upper()[0]

if tipo_carne == 'F':
    tipo_carne = 'Filé Duplo'
    kilo_carne = float(input(f'Informe quantos kilos de {tipo_carne} o cliente irá levar: '))

    if kilo_carne <= 5:
        preço_kilo = 4.90

    elif kilo_carne > 5:
        preço_kilo = 5.80

elif tipo_carne == 'A':
    tipo_carne = 'Alcanha'
    kilo_carne = float(input(f'Informe quantos kilos de {tipo_carne} o cliente irá levar: '))

    if kilo_carne <= 5:
        preço_kilo = 5.90

    elif kilo_carne > 5:
        preço_kilo = 6.80

elif tipo_carne == 'P':
    tipo_carne = 'Picanha'
    kilo_carne = float(input(f'Informe quantos kilos de {tipo_carne} o cliente irá levar: '))

    if kilo_carne <= 5:
        preço_kilo = 6.90
    elif kilo_carne > 5:
        preço_kilo = 7.80

preço_total = kilo_carne * preço_kilo
if preço_total < 10:
    preço_total_str = f'R$0{preço_total:.2f}'.replace('.', ',')
else:
    preço_total_str = f'R${preço_total:.2f}'.replace('.', ',')

desconto_cartão = 5 / 100 * preço_total
if desconto_cartão < 10:
    desconto_cartão_str = f'R$0{desconto_cartão:.2f}'.replace('.', ',')
else:
    desconto_cartão_str = f'R${desconto_cartão:.2f}'.replace('.', ',')

preço_final = preço_total - desconto_cartão
if preço_final < 10:
    preço_final_str = f'R$0{preço_final:.2f}'.replace('.', ',')
else:
    preço_final_str = f'R${preço_final:.2f}'.replace('.', ',')
# ------------------------------------------------------------------------
preço_total_texto = "Preço Total"
tam_preço_total_texto = 50 - len(preço_total_texto)

desconto_texto = "Desconto de 5% do Cartão"
tam_desconto_texto = 50 - len(desconto_texto)

preço_texto  = "Preço a Pagar"
tam_preço_texto =  50 - len(preço_texto)

print()
print(f"{f'{kilo_carne}Kg de {tipo_carne}'}")
print('=' * 60)

print(f'{preço_total_texto}{"." * (tam_preço_total_texto)}{preço_total_str}')

print(f'{desconto_texto}{"." * (tam_desconto_texto)}{desconto_cartão_str}')

print(f'{preço_texto}{"." * (tam_preço_texto)}{preço_final_str}')






