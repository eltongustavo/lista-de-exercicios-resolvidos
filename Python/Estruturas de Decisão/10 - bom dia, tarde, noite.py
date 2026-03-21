turno = input('Informe em que turno você estuda (M - Matutino, V- Vespertino, N - Noturno): ').upper()
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Turno inválido!')
