salario_atual_int = float(input('Digite qual seu salário atual: '))
salario_atual_str = f'R${salario_atual_int:.2f}'.replace('.', ',')
aumento_valor = 0
aumento_string = ''

if 0 < salario_atual_int <= 280:
    aumento_valor = 20 / 100 * salario_atual_int
    aumento_valor_str = f'R${aumento_valor:.2f}'.replace('.', ',')
    aumento_string = f'20%'
elif 280 < salario_atual_int <= 700:
    aumento_valor = 15 / 100 * salario_atual_int
    aumento_valor_str = f'R${aumento_valor:.2f}'.replace('.', ',')
    aumento_string = f'15%'
elif 700 < salario_atual_int <= 1500:
    aumento_valor = 10 / 100 * salario_atual_int
    aumento_valor_str = f'R${aumento_valor:.2f}'.replace('.', ',')
    aumento_string = f'10%'
elif salario_atual_int > 1500:
    aumento_valor = 5 / 100 * salario_atual_int
    aumento_valor_str = f'R${aumento_valor:.2f}'.replace('.', ',')
    aumento_string = f'5%'
else:
    print('Salário Inválido!')

salario_ajustado = salario_atual_int + aumento_valor
salario_ajustado_str = f'R${salario_ajustado:.2f}'.replace('.', ',')

print(f'''Antes do reajuste: {salario_atual_str}
Porcentual de aumento: {aumento_string}
Valor aumentado: {aumento_valor_str}
Novo salário: {salario_ajustado_str}''')



