while True:
    try:
        num = int(input('Digite um número entre 0 e 10: '))
    except ValueError:
        print()
        print('\033[31mPor favor informe um valor do tipo inteiro.\033[m')
        print()
    else:
        if 0 <= num <= 10:
            print(f'O número digitado foi \033[32m{num}\033[m')
            break
        else:
            print('Por favor informe um valor entre 0 e 10.')

print('\033[33mFIM!\033[m')
