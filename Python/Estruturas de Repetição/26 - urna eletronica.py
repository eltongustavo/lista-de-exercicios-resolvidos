votos_eleitor_um = votos_eleitor_dois = votos_eleitor_três = 0
quantidade_eleitores = int(input('Digite quantos eleitores votarão: '))
for x in range(1, quantidade_eleitores + 1):
    voto = input(f'Voto do eleitor {x} / (1/2/3): ')
    while voto not in '123':
        print()
        print('Voto Inválido!')
        print()
        voto = input(f'Voto do eleitor {x} / (1/2/3): ')
    if voto == '1':
        votos_eleitor_um += 1
    elif voto == '2':
        votos_eleitor_dois += 1
    elif voto == '3':
        votos_eleitor_três += 1
print('Resultado das eleições:\n'
      f'Eleitor Um   : {votos_eleitor_um} votos\n'
      f'Eleitor Dois : {votos_eleitor_dois} votos\n'
      f'Eleitor Três : {votos_eleitor_três} votos')





