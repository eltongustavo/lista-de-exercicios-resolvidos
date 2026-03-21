number_factorial = int(input('Enter a number: '))
print(f'{number_factorial}! = ', end='')

for x in range(number_factorial, 1, - 1):
    number_factorial = number_factorial * (x - 1)
print(number_factorial)
