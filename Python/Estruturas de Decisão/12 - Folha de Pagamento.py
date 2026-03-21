horas_trabalhadas = int(input('Digite quantas horas você trabalhou nesse mês: '))
valor_hora = float(input('Digite qual é o valor da hora trabalhada na sua empresa: '))

print()

salario_bruto = float(horas_trabalhadas * valor_hora)
salario_bruto_str = f'R${salario_bruto:.2f}'.replace('.', ',')

if salario_bruto <= 900:
    imposto_renda = 0
    imposto_renda_str = f'R${imposto_renda:.2f}'.replace('.', ',')
    IR = '0'
elif 900 < salario_bruto <= 00:
    imposto_renda = 5 / 100 * salario_bruto
    imposto_renda_str = f'R${imposto_renda:.2f}'.replace('.', ',')
    IR = '5'
elif 00 < salario_bruto <= 2500:
    imposto_renda = 10 / 100 * salario_bruto
    imposto_renda_str = f'R${imposto_renda:.2f}'.replace('.', ',')
    IR = '10'
elif salario_bruto > 2500:
    imposto_renda = 20 / 100 * salario_bruto
    imposto_renda_str = f'R${imposto_renda:.2f}'.replace('.', ',')
    IR = '20'

inss = 10 / 100 * salario_bruto
inss_str = f'R${inss:.2f}'.replace('.', ',')

fgts = 11 / 100 * salario_bruto
fgts_str = f'R${fgts:.2f}'.replace('.', ',')

total_descontos = inss + imposto_renda
total_descontos_str = f'R${total_descontos:.2f}'.replace('.', ',')

salario_liquido = salario_bruto - (inss + imposto_renda)
salario_liquido_str = f'R${salario_liquido:.2f}'.replace('.', ',')

print(f'{f"Salário Bruto [{horas_trabalhadas}h * R${valor_hora:.2f}]":<30}:{salario_bruto_str}')
print(f'{f"(-) Imposto de Renda ({IR}%)":<30}:{imposto_renda_str}')
print(f'{"(-) INSS (10%)":<30}:{inss_str}')
print(f'{"FGTS":<30}:{fgts_str}')
print(f'{"Total de Descontos":<30}:{total_descontos_str}')
print(f'{"Salário Liquido":<30}:{salario_liquido_str}')





