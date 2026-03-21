num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite um número: '))
num_3 = float(input('Digite um número: '))

maior = menor = num_1
if num_2 > maior:
    maior = num_2
else:
    menor = num_2
if num_3 > maior:
    maior = num_3
else:
    if num_3 < num_2 and num_3 < num_1:
        menor = num_3
print(f'Entre {num_1} / {num_2} / {num_3}\n'
      f'{maior} é o maior\n'
      f'{menor} é o menor')
