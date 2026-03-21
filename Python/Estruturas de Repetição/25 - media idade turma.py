quantidade_pessoas = int(input('Digite quantas pessoas serão questionadas: '))
lista_de_idades = []

for x in range(0, quantidade_pessoas):
    lista_de_idades.append(int(input(f'Qual a idade da pessoa de número {x + 1}: ')))

media_idades = sum(lista_de_idades) / quantidade_pessoas
if 0 < media_idades <= 25:
    print(f'De acordo com a média de idade {int(media_idades)} anos, o grupo de pessoas foi considerado jovem!')
elif 26 < media_idades <= 60:
    print(f'De acordo com a média de idade {int(media_idades)} anos, o grupo de pessoas foi considerado adulto!')
elif media_idades > 60:
    print(f'De acordo com a média de idade {int(media_idades)} anos, o grupo de pessoas foi considerado idoso!')


