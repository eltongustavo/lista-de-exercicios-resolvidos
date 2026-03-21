lista_situações = [0, 0, 0, 0]
quantidade_mouses = 0
while True:
    identificação_mouse = str(input('Digite o código de identificação do mouse: '))

    necessita_esfera = str(input('O mouse necessita de uma nova esfera? (S/N) ')).upper()[0]
    while necessita_esfera not in 'SN':
        print()
        print('\033[31mPor favor digite \033[m\033[32m"S"\033[m \033[31mou\033[m \033[32m"N"\033[m')
        print()
        necessita_esfera = str(input('O mouse necessita de uma nova esfera? (S/N) ')).upper()[0]
    if necessita_esfera == 'S':
        lista_situações[0] += 1

    necessita_limpeza = str(input('O mouse necessita de limpeza? (S/N) ')).upper()[0]
    while necessita_limpeza not in 'SN':
        print()
        print('\033[31mPor favor digite \033[m\033[32m"S"\033[m \033[31mou\033[m \033[32m"N"\033[m')
        print()
        necessita_limpeza = str(input('O mouse necessita de limpeza? (S/N) ')).upper()[0]
    if necessita_limpeza == 'S':
        lista_situações[1] += 1

    necessita_novo_cabo_conector = str(input('O mouse necessita trocar de cabo ou conector? (S/N) ')).upper()[0]
    while necessita_novo_cabo_conector not in 'SN':
        print()
        print('\033[31mPor favor digite \033[m\033[32m"S"\033[m \033[31mou\033[m \033[32m"N"\033[m')
        print()
        necessita_novo_cabo_conector = str(input('O mouse necessita trocar de cabo ou conector? (S/N) ')).upper()[0]
    if necessita_novo_cabo_conector == 'S':
        lista_situações[2] += 1

    quebrado_inutilizado = str(input('O mouse está quebrado ou inutilizado? (S/N) ')).upper()[0]
    while quebrado_inutilizado not in 'SN':
        print()
        print('\033[31mPor favor digite \033[m\033[32m"S"\033[m \033[31mou\033[m \033[32m"N"\033[m')
        print()
        quebrado_inutilizado = str(input('O mouse está quebrado ou inutilizado? (S/N) ')).upper()[0]
    if quebrado_inutilizado == 'S':
        lista_situações[3] += 1

    quantidade_mouses += 1

    mais_mouse = str(input('Tem mais mouses a serem cadastrados? (S/N) ')).upper()[0]
    while mais_mouse not in 'SN':
        print()
        print('\033[31mPor favor digite \033[m\033[32m"S"\033[m \033[31mou\033[m \033[32m"N"\033[m')
        print()
        mais_mouse = str(input('Tem mais mouses a serem cadastrados? (S/N) ')).upper()[0]
    if mais_mouse == 'N':
        break
    else:
        print()
        print('\033[32mMouse adicionado com sucesso ao sistema!\033[m')
        print()

print()
print('Os resultados estão abaixo!')
print()
print(f'\033[33m{lista_situações[0]}\033[m mouses necessitam de uma \033[33mnova esfera\033[m, isso é equivalente a \033[32m{lista_situações[0] * 100 / quantidade_mouses:.2f}%\033[m de todos os {quantidade_mouses} mouses cadastrados')
print()
print(f'\033[33m{lista_situações[1]}\033[m mouses \033[33mnecessitam de limpeza\033[m, isso é equivalente a \033[32m{lista_situações[1] * 100 / quantidade_mouses:.2f}%\033[m de todos os {quantidade_mouses} mouses cadastrados')
print()
print(f'\033[33m{lista_situações[2]}\033[m mouses necessitam de \033[33mtroca do cabo ou conector\033[m, isso é equivalente a \033[32m{lista_situações[2] * 100 / quantidade_mouses:.2f}%\033[m de todos os {quantidade_mouses} mouses cadastrados')
print()
print(f'\033[33m{lista_situações[3]}\033[m mouses \033[33mestão quebrados ou inutilizados\033[m, isso é equivalente a \033[32m{lista_situações[3] * 100 / quantidade_mouses:.2f}%\033[m de todos os {quantidade_mouses} mouses cadastrados')





