print("""MODELO: 00/00/0000 obs: USE A BARRA
Digite sua data de nascimento: """, end='')
dia, mes, ano = map(int, input().split('/'))

if dia < 1 or dia > 31:
    print("\033[31mDia Inválido!\033[m")
    exit()
    
if mes == 1:
    mes = "Janeiro"
elif mes == 2:
    mes = "Fevereiro"
elif mes == 3:
    mes = "Março"
elif mes == 4:
    mes = "Abril"
elif mes == 5:
    mes = "Maio"
elif mes == 6:
    mes = "Junho"
elif mes == 7:
    mes = "Julho"
elif mes == 8:
    mes = "Agosto"
elif mes == 9:
    mes = "Setembro"
elif mes == 10:
    mes = "Outubro"
elif mes == 11:
    mes = "Novembro"
elif mes == 12:
    mes = "Dezembro"
else:
    print("\033[31mMês Inválido!\033[m")
    exit()
print(f'{dia} de {mes} de {ano}')
    

    
        