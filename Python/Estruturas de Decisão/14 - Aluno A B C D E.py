nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2

nota_final = ''
sit_aluno = ''

if 9 <= media <= 10:
    nota_final = 'A'
    sit_aluno = 'Aprovado'
elif 7.5 <= media < 9:
    nota_final = 'B'
    sit_aluno = 'Aprovado'
elif 6 <= media < 7.5:
    nota_final = 'C'
    sit_aluno = 'Aprovado'
elif 4 <= media < 6:
    nota_final = 'D'
    sit_aluno = 'Reprovado'
elif 0 <= media < 4:
    nota_final = 'E'
    sit_aluno = 'Reprovado'
else:
    print('Erro ao avaliar as notas.')
print(f'Com uma média de {media}, o aluno recebeu a classificação {nota_final}, portanto ele está {sit_aluno}!')
