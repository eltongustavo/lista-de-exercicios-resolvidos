gabarito = ''
print('Para o professor, determine o gabarito da prova: ')
print('=' * 50)
for x in range(1, 11):
    resposta = str(input(f'Digite a resposta da questão {x}: (A/B/C/D)')).upper()[0]
    while resposta not in 'ABCD':
        resposta = str(input(f'Digite a resposta da questão {x}: (A/B/C/D)')).upper()[0]
    gabarito += resposta

print('=' * 50)
print()
notas = []
respostas_aluno = ''
quantidade_acertos = 0
quantidade_alunos = 0
while True:
    for x in range(1, 11):
        while True:
            try:
                questão = str(input(f'Digite a resposta da questão de número {x}: (A/B/C/D) ')).upper()[0]
            except IndexError:
                print('Resposta vázia inválida.')
                continue
            else:
                while questão not in 'ABCD':
                    try:
                        questão = str(input(f'Digite a resposta da questão de número {x}: (A/B/C/D) ')).upper()[0]
                    except IndexError:
                        print('Resposta vázia inválida.')
                        continue
                    else:
                        respostas_aluno += questão
                        break

                respostas_aluno += questão
                break

    for x in range(len(gabarito)):
        if gabarito[x] == respostas_aluno[x]:
            quantidade_acertos += 1
    notas.append(quantidade_acertos)

    print(f'O aluno acertou {quantidade_acertos} questões do total de 10.')
    print()
    quantidade_alunos += 1

    mais_alunos = str(input('Mais alunos responderão a prova? (S/N): ')).upper()[0]
    print()
    while mais_alunos not in 'SN':
        mais_alunos = str(input('Mais alunos responderão a prova? (S/N): ')).upper()[0]
        print()
    if mais_alunos == 'N':
        print()
        break

maior_nota = menor_nota = notas[0]
media_notas = sum(notas) / len(notas)
for x in notas:
    if x > maior_nota:
        maior_nota = x
    if x < menor_nota:
        menor_nota = x


print(f'{quantidade_acertos} alunos responderam a essa prova.')
print('=' * 50)
print(f'A maior nota entre os alunos foi {maior_nota} acertos.\n'
      f'Já a menor nota foi de {menor_nota} acertos.')
print('=' * 50)
print(f'A média de notas da turma foi de {media_notas} acertos.')
print()

print('=' * 50)
print('O gabarito final é: ')
for y, x in enumerate(range(len(gabarito))):
    print(f'{y + 1} - {gabarito[x]}')
print('=' * 50)
