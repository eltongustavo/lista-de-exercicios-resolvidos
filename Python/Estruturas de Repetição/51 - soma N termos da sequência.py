first = second = 1
counter = 0
divisions = []
limit = int(input('Quantas vezes a sequência será mostrada? '))
while counter < limit:
    print(f'{first}/{second}', end='')
    division_first_by_second = first / second
    divisions.append(division_first_by_second)
    if counter + 1 < limit:
        print(' + ', end='')
    first += 1
    second += 2
    counter += 1
print()
print(f'A soma de todas as divisões feitas é de {sum(divisions)}')


