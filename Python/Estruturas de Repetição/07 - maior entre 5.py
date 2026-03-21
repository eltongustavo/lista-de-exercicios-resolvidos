num = int(input('Digite um número: '))
maior = num
for x in range(0, 4):
    num_teste = int(input('Digite um número: '))
    if num_teste > maior:
        maior = num_teste
print(f'Dos números digitados, o maior foi: {maior}')

    

