num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))

if num_1 > num_2:
    greater = num_1
    less = num_2

elif num_1 < num_2:
    greater = num_2
    less = num_1

else:
    greater = (num_1 + num_2) / 2
    less = (num_1 + num_2) / 2

for x in range(less + 1, greater):
    print(x, end=' ')