altura = float(input('Digite sua altura: '))
peso_ideal_man = (72.7 * altura) - 58
peso_ideal_woman = (62.1 * altura) - 44.7
print('''De acordo com as formulas:
------------------------------------------
PI_Homem = (72.7 * altura) - 58
PI_Mulher = (62.1 * altura) - 44.7
------------------------------------------''')
print('Seu peso ideal é de:')
print(f'''Peso ideal Homem = {peso_ideal_man:.1f}Kg
Peso ideal Mulher = {peso_ideal_woman:.1f}Kg''')
