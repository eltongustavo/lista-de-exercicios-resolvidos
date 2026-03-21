salario_1995 = int(input('Digite qual era o salário do trabalhador em 1995: '))
porcentagem_aumento = 1.5
salario_1996 = salario_1995 + (porcentagem_aumento / 100 * salario_1995)

for x in range(0, 25):
    salario_1996 += ((porcentagem_aumento * 2) / 100 * salario_1996)
print(f'O salário atual em 2022 desse trabalhador é de R${salario_1996:.2f}')




