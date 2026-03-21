lista_num_altura = []
lista_auxiliar = []
for x in range(1, 11):
    numero = x
    altura = float(input(f'Digite a altura do aluno {numero}: '))
    lista_auxiliar.append(numero)
    lista_auxiliar.append(altura)
    lista_num_altura.append(lista_auxiliar[:])
    lista_auxiliar.clear()

maior_altura = menor_altura = lista_num_altura[0][1]

for x in lista_num_altura:
    if x[1] > maior_altura:
        maior_altura = x[1]
        num_maior_altura = x[0]
    elif x[1] < menor_altura:
        menor_altura = x[1]
        num_menor_altura = x[0]

print('De acordo com a lista de 10 alunos recebida:\n'
      f'O aluno {num_maior_altura} tem a maior altura, com {maior_altura}m\n'
      f'O aluno {num_menor_altura} tem a menor altura, com {menor_altura}m')
