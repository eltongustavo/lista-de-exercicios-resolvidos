from curses.ascii import isalnum

listaCaracteres = []

cpf = input("""MODELO: XXX.XXX.XXX-XX
Digite seu CPF: """)

if len(cpf) != 14:
    print("\033[31mCPF Inválido!\033[m")
    exit()

for x in range(0, len(cpf)):
    listaCaracteres.append(cpf[x])

for x in listaCaracteres:
    if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
        listaCaracteres.remove('.')
        listaCaracteres.remove('.')
        listaCaracteres.remove('-')
        break
    else:
        print("\033[31mCPF Inválido!\033[m")
        exit()

numeros = ''
for x in listaCaracteres:
    numeros += x

if numeros.isnumeric == False:
    print("\033[31mCPF Inválido!\033[m")
    exit()
else:
    print("CPF VÁLIDO!")
