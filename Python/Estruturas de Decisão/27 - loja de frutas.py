morango_kg = float(input('Digite quantos kilos de morango o cliente irá levar: '))
maçã_kg = float(input('Digite quantos kilos de maçã o cliente irá levar: '))

if morango_kg <= 5:
    preço_kilo_morango = 2.50
elif morango_kg > 5:
    preço_kilo_morango = 2.20

if maçã_kg <= 5:
    preço_kilo_maçã = 1.80
elif maçã_kg > 5:
    preço_kilo_maçã = 1.50

soma_kilo = morango_kg + maçã_kg
pagamento = (morango_kg * preço_kilo_morango) + (maçã_kg * preço_kilo_maçã)

if soma_kilo > 8 or pagamento > 25:
    pagamento = pagamento - (10 / 100 * pagamento)
pagamento_str = f'R${pagamento:.2f}'.replace('.', ',')

print(f'O cliente pediu {morango_kg}Kg de morango e {maçã_kg}Kg de maçã, o preço a ser pago é de {pagamento_str}')