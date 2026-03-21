soma = 0
for x in range(0, 5):
    num = int(input('Digite um número: '))
    soma += num
media = soma / 5
print(f'A soma dos 5 números: {soma}\n'
      f'A média dos 5 números: {media}')