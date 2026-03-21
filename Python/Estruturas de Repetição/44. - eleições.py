nomes_candidatos = []
votos_candidato_um = votos_candidato_dois = votos_candidato_três = votos_candidato_quatro =\
    votos_nulos = votos_em_branco = 0

votos_candidatos = []
for x in range(0, 4):
    nome = str(input(f'Insira o nome do candidato {x + 1}: ')).title()
    nomes_candidatos.append(nome)
nomes_candidatos.append('Votos Nulos')
nomes_candidatos.append('Votos em Branco')
print('Eleição - Opções Abaixo:')
for y, x in enumerate(nomes_candidatos):
    print(f'{y + 1} - {x:20}')

print()
while True:
    voto = str(input('Escolha a opção de voto: '))[0]
    while voto not in '123456':
        voto = str(input('Escolha a opção de voto: '))[0]
    if voto == '1':
        votos_candidato_um += 1
    elif voto == '2':
        votos_candidato_dois += 1
    elif voto == '3':
        votos_candidato_três += 1
    elif voto == '4':
        votos_candidato_quatro += 1
    elif voto == '5':
        votos_nulos += 1
    elif voto == '6':
        votos_em_branco += 1
    print(f'\033[32mOpção {voto} validada com sucesso!\033[m')
    print()
    continuar = str(input('\033[33mAinda existem eleitores para votar? (S/N): \033[m')).upper()[0]
    print()
    while continuar not in 'SN':
        continuar = str(input('\033[33mAinda existem eleitores para votar? (S/N): \033[m')).upper()[0]
        print()
    if continuar == 'S':
        continue
    else:
        votos_candidatos.append(votos_candidato_um)
        votos_candidatos.append(votos_candidato_dois)
        votos_candidatos.append(votos_candidato_três)
        votos_candidatos.append(votos_candidato_quatro)
        votos_candidatos.append(votos_nulos)
        votos_candidatos.append(votos_em_branco)
        break

print(f'{"Nomes Candidatos":24}{"Quantidade de Votos"}')
print('=' * 44)
for y, x in enumerate(nomes_candidatos):
    tamanho_x = len(str(x))
    quantidade_pontos = 38 - tamanho_x
    reticências_str = ('.' * quantidade_pontos)
    print(f'{y + 1} - {x}', end= reticências_str)
    print(votos_candidatos[y])





