# Método Padrão

nota_1 = float(input('Digite a nota do bimestre 1: '))
nota_2 = float(input('Digite a nota do bimestre 2: '))
nota_3 = float(input('Digite a nota do bimestre 3: '))
nota_4 = float(input('Digite a nota do bimestre 4: '))
soma = nota_1 + nota_2 + nota_3 + nota_4
media = soma / 4
print(f'A média das notas recebidas foi de {media}')

# Método com Apenas duas variáveis

nota = float(input('Digite a nota do bimestre 1: '))
soma_notas = nota
nota = float(input('Digite a nota do bimestre 2: '))
soma_notas += nota
nota = float(input('Digite a nota do bimestre 3: '))
soma_notas += nota
nota = float(input('Digite a nota do bimestre 4: '))
soma_notas += nota
print(f'A média das notas recebidas foi de {soma_notas / 4}')

# Método com Laço de Repetição

soma_notas = 0
for x in range(0, 4):
    nota = int(input(f'Digite a nota do bimestre {x + 1}: '))
    soma_notas += nota
print(f'A média das notas recebidas foi de {soma_notas / 4}')


