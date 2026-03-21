while True:

    usuário = str(input('Digite seu nome de usuário: '))
    senha = str(input('Digite sua senha: '))

    if usuário == senha:
        print('Por favor digite usuário e senha diferentes entre si.')
        continue

    else:
        break
print()
print(f'O usuário digitado foi \033[32m{usuário}\033[m')
print(f'A senha digitada foi \033[32m{senha}\033[m')
