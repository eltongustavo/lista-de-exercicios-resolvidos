from time import sleep
lista_salarios = []
while True:
    salario_colaborador = float(input('Digite o seu salário: R$'))
    if salario_colaborador < 0:
        print()
        print('\033[31mSalário Inválido!\033[m')
        print()
        continue
    elif salario_colaborador == 0:
        sleep(1)
        print()
        print('\033[32mTodos os salários anteriores foram adicionados ao sistema!\033[m')
        print()
        print('Carregando resultados...')
        sleep(2)
        break
    else:
        lista_salarios.append(salario_colaborador)

lista_abonos = []
for x in lista_salarios:
    if 20 / 100 * x < 100:
        lista_abonos.append(100)
    else:
        lista_abonos.append(20 / 100 * x)

for y, x in enumerate(lista_salarios):
    print(f'Para o salário de \033[32mR${x:.2f}\033[m o abono será de \033[32mR${lista_abonos[y]:.2f}\033[m')
print()
print(f'Foram um total de {len(lista_abonos)} colaboradores!')
print(f'O valor total pago em abonos foi de \033[32mR${sum(lista_abonos):.2f}\033[m')
print(f'O maior valor de abono pago foi de \033[32mR${max(lista_abonos):.2f}\033[m')
