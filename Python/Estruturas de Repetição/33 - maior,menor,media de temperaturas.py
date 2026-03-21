conjunto_temperaturas = []
while True:
    leitor_temperatura = float(input('Digite a temperatura em graus Cº : '))
    conjunto_temperaturas.append(leitor_temperatura)
    continuar_programa = input('Quer continuar? (S/N): ').upper()[0]
    while continuar_programa not in 'SN':
        continuar_programa = input('Quer continuar? (S/N): ').upper()[0]
    if continuar_programa == 'N':
        break

maior = menor = conjunto_temperaturas[0]
media = sum(conjunto_temperaturas) / len(conjunto_temperaturas)
for x in conjunto_temperaturas:
    if x >= maior:
        maior = x
    if x <= menor:
        menor = x

print('De acordo com os dados recebidos:\n'
      f'A maior temperatura foi de {maior:.1f}º\n'
      f'A menor temperatura foi de {menor:.1f}º\n'
      f'A média de temperaturas foi de {media:.1f}º')
