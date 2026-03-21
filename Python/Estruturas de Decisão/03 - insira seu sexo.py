sexo = str(input('Digite seu sexo: (M/F/I) ')).upper()
if sexo == 'M':
    print('O sexo selecionado foi: MASCULINO')
elif sexo == 'F':
    print('O sexo selecionado foi FEMININO')
elif sexo == 'I':
    print('O sexo selecionado foi INDEFINIDO')
else:
    print('Nenhum sexo válido foi selecionado')
