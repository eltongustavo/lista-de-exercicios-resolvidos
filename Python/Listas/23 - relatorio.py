def transformar_em_megabytes(valor_em_kilobytes):
    Kbytes = valor_em_kilobytes
    Mbytes = Kbytes / 1000000
    return Mbytes

print('ACME Inc.                              Uso do espaço em disco pelos usuários')
print('-' * 80)
print(f'{"Nr.":5}{"Usuário":15}{"Espaço Utilizado":22}{"% do uso"}')
print()

with open('usuarios.txt', 'r') as arquivo:
    soma = 0
    lista_bytes = []
    lista = arquivo.readlines()

    for linha in lista:
        lista_bytes.append(int(linha[15:]))
        
    lista_mega = []
    for x in lista_bytes:
        lista_mega.append(transformar_em_megabytes(x))

    for x, linha in enumerate(lista):
        print(f'{x + 1:<5}{linha[0:15]:15}', end='')
        Mb = transformar_em_megabytes(int(linha[15:]))
        print(f"{f'{Mb:.2f} Mb':22}", end='')
        print(f"{lista_mega[x] * 100 / sum(lista_mega):.2f}", '%')

    print()
    
    print(f'Espaço total ocupado: {sum(lista_mega):.2f} MB')
    print(f'Espaço médio ocupado: {sum(lista_mega) / len(lista_mega):.2f} MB')

        
        
        







        

    


