even_counter = odd_counter = 0
for x in range(0, 10):
    number = int(input('Enter a number: '))
    if number % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1
print(f'In even numbers counter, there are {even_counter} numbers.')
print(f'In odd numbers counter, there are {odd_counter} numbers.')
