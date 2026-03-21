horas_trabalhadas = int(input('Quantas horas você trabalhou nesse mês: '))
valor_hora = float(input('Digite quanto você ganha por hora: '))
salario_bruto = horas_trabalhadas * valor_hora
salario_liquido = salario_bruto - (24 / 100 * salario_bruto)
print(f'''Seu salário bruto é de {salario_bruto:.2f}R$
Você pagou 11%, ou seja {11 / 100 * salario_bruto:.2f}R$, para o Imposto de Renda
Você pagou 8%, ou seja {8 / 100 * salario_bruto:.2f}R$, para o INSS
Você pagou 5%, ou seja {5 / 100 * salario_bruto:.2f}R$, para o Sindicato
E o seu Salário Liquido é de {salario_liquido:.2f}R$''')


