first = 1
second = 0
counter = 1
limit = int(input('Quantas vezes a sequência será mostrada? '))
print('H = ', end='')
while counter < limit:
    if first == 1 and second == 0:
        print(first, end=' + ')
    if second == 0:
        second += 2
    print(f'{first}/{second}', end='')
    if counter + 1 < limit:
        print(' + ', end='')
    second += 1
    counter += 1

