first = second = 1
counter = 0
limit = int(input('Quantas vezes a sequência será mostrada? '))
while counter < limit:
    print(f'{first}/{second}', end='')
    if counter + 1 < limit :
        print(' + ', end='')
    first += 1
    second += 2
    counter += 1
