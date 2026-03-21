from math import pi

# Calculador de área, usando pi como 3.14
raio = float(input('Informe o valor do raio(m): '))
area = 3.14 * (raio ** 2)
print(f'O valor da área é de {area:.2f}m²')

# Calculador de área, usando o valor pi da biblioteca math
raio2 = float(input('Informe o valor do raio(m): '))
area2 = pi * (raio ** 2)
print(f'O valor da área é de {area2:.2f}m²')

