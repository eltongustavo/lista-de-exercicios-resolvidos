contador_culpa = 0

p1 = input('Telefonou para a vítima? (S/N): ').upper()[0]
while p1 not in 'SN':
    p1 = input('Telefonou para a vítima? (S/N): ').upper()[0]
if p1 == 'S':
    contador_culpa += 1

p2 = input('Esteve no local do crime? (S/N): ').upper()[0]
while p2 not in 'SN':
    p2 = input('Esteve no local do crime? (S/N): ').upper()[0]
if p2 == 'S':
    contador_culpa += 1

p3 = input('Mora perto da vítima? (S/N): ').upper()[0]
while p3 not in 'SN':
    p3 = input('Mora perto da vítima? (S/N): ').upper()[0]
if p3 == 'S':
    contador_culpa += 1

p4 = input('Devia pra vítima? (S/N): ').upper()[0]
while p4 not in 'SN':
    p4 = input('Devia pra vítima? (S/N): ').upper()[0]
if p4 == 'S':
    contador_culpa += 1

p5 = input('Já trabalhou com a vítima? (S/N): ').upper()[0]
while p5 not in 'SN':
    p5 = input('Já trabalhou com a vítima? (S/N): ').upper()[0]
if p5 == 'S':
    contador_culpa += 1

if contador_culpa == 0 or contador_culpa == 1:
    print('O entrevistado foi considerado inocente!')

elif contador_culpa == 2:
    print('O entrevistado foi considerado Suspeito!')

elif contador_culpa == 3 or contador_culpa == 4:
    print('O entrevistado foi considerado Cúmplice!')

elif contador_culpa == 5:
    print('O entrevistado foi considerado Assassino!')

else:
    print('Erro no sistema!')