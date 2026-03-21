base = int(input('Enter the base of the exponency: '))
base_aux = base
exponent = int(input('Enter the exponent of the exponency: '))

for x in range(0, exponent - 1):
    result = base * base_aux
    base = base * base_aux

print(f'The result of the exponency {base_aux} to the power {exponent} is {result}.')

