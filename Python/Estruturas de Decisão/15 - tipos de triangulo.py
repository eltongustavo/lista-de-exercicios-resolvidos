lado_1 = float(input('Digite o tamanho do primeiro lado do triângulo: '))
lado_2 = float(input('Digite o tamanho do segundo lado do triângulo: '))
lado_3 = float(input('Digite o tamnho do terceiro lado do triângulo: '))

if lado_1 == lado_2 == lado_3:
    print(f'Triângulo Equilátero com lados medindo {lado_1}cm')

elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
    print(f'Trângulo Escaleno, com lados: {lado_1}cm / {lado_2}cm / {lado_3}cm')

elif lado_1 == lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
    # lado 1 e 2 iguais
    print(f'Triângulo Isosceles, com dois lados medindo {lado_1}cm e outro lado medindo {lado_3}cm')

elif lado_1 == lado_3 and lado_1 != lado_2 and lado_3 != lado_2:
    # lado 1 e 3 iguais
    print(f'Triângulo Isosceles, com dois lados medindo {lado_1}cm e outro lado medindo {lado_2}cm')

elif lado_2 == lado_3 and lado_2 != lado_1 and lado_3 != lado_1:
    # lado 2 e 3 iguais
    print(f'Triângulo Isosceles, com dois lados medindo {lado_2}cm e outro lado medindo {lado_1}cm')

else:
    print('Triângulo não pode ser classificado!')


