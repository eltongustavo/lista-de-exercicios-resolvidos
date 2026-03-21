nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2
if media == 10:
    print(f'{media}, Nota Perfeita! Aprovado.')
elif 7 <= media < 10:
    print(f'{media}, Muito Bem! Aprovado.')
elif media < 7:
    print(f'{media}, Que Pena! Reprovado.')

