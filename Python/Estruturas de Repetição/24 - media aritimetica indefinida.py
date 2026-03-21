quantidade_notas = int(input('Informe quantas notas serão usadas para fazer a média: '))
lista_de_notas = []
for x in range(0, quantidade_notas):
    lista_de_notas.append(float(input(f'Digite a nota de número {x + 1}: ')))
media_aritmética = sum(lista_de_notas) / quantidade_notas
print(f'A média aritmética das {quantidade_notas} notas foi de {media_aritmética:.1f}')
