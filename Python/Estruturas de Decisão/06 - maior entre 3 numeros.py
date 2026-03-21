num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite um número: '))
num_3 = float(input('Digite um número: '))
maior = num_1
if num_2 > maior:
    maior = num_2
if num_3 > maior:
    maior = num_3
print(f'Entre \033[31m{num_1}\033[m / \033[31m{num_2}\033[m / \033[31m{num_3}\033[m\n'
      f'\033[32m{maior}\033[m é o maior deles.')



