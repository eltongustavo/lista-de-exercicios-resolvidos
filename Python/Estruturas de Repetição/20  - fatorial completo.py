while True:
    number_factorial = int(input('Enter a new number: '))
    if number_factorial < 0 or number_factorial > 16:
        print('Digite um número entre 0 e 16.')
        continue

    print(f'{number_factorial}! : ', end='')
    for x in range(number_factorial, 0, -1):
        print(f'{x}', end='')
        if x != 1:
            print(' x ', end='')
        else:
            print(' = ', end='')

    for x in range(number_factorial, 1, - 1):
        number_factorial = number_factorial * (x - 1)
    print(number_factorial)

    confirmação = input('New number? (s/n)').upper()[0]
    while confirmação not in 'SN':
        confirmação = input('New number? (s/n)').upper()[0]
    if confirmação == 'N':
        break
