num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))

if num_1 > num_2:
    greater = num_1
    less = num_2
elif num_2 > num_1:
    greater = num_2
    less = num_1
else:
    greater = less = num_1

sum_numbers = 0
for x in range(less + 1, greater):
    print(x, end=' ')
    sum_numbers += x

print(f'The sum of the numbers is {sum_numbers}')

