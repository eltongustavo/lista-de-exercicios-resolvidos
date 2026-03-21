num = int(input('Digite o número que você quer saber se é Par ou Impar: '))
resto = num % 2
if resto == 0:
    print(f'{num} é Par!')
else:
    print(f'{num} é Impar!')