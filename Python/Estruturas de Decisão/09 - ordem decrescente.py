num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))
num_3 = int(input('Digite mais um número: '))

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
lista = [num_1, num_2, num_3]
for x in lista:
    if x != maior and x != menor:
        meio = x
        
print(f'Os números digitados em ordem crescente ficam assim:\n'
      f'{menor} - {meio} - {maior}')

