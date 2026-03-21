while True:
    nome = input('Digite um nome com mais de 3 caracteres: ')
    if len(nome) < 4:
        print('Nome Inválido!')
        continue

    idade = int(input('Digite uma idade (0 - 150): '))
    if idade < 0 or idade > 150:
        print('Idade Inválida!')
        continue

    salário = float(input('Digite um salário: R$'))
    if salário < 0:
        print('Salário Inválido!')
        continue

    sexo = input('Digite um sexo: (F/M)').upper()[0]
    if sexo not in 'FM':
        print('Sexo Inválido!')
        continue

    estado_civil = input('Digite seu estado civil (S / C / V / D): ').upper()
    if estado_civil not in 'SCVD':
        print('Estado Civil Inválido!')
        continue
    break
    
print()
print(f'''As informações seguintes foram validadas:
Nome: {nome}
Idade: {idade}
Salário: {salário:.2f}
Sexo: {sexo}
Estado Civil: {estado_civil}''')
