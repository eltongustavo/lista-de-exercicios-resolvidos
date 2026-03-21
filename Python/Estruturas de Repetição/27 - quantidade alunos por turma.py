quantidade_turmas = int(input('Digite quantas turmas existem na escola: '))
lista_alunos_turma = []
for x in range(0, quantidade_turmas):
    alunos_turma = int(input(f'Quantos alunos na turma {x + 1}: '))
    while alunos_turma < 0 or alunos_turma > 40:
        print()
        print('Turma não pode ter mais de 40 alunos.')
        print()
        alunos_turma = int(input(f'Quantos alunos na turma {x + 1}: '))
    lista_alunos_turma.append(alunos_turma)
media_alunos_turma = sum(lista_alunos_turma) / len(lista_alunos_turma)
print(f'A média de alunos na escola é de aproximadamente {int(media_alunos_turma)} alunos por turma.')


