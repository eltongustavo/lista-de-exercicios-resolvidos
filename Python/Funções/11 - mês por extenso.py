Dia = int(input("Digite o dia em que nasceu: "))
Mês = int(input("Digite o mês em que nasceu: "))
Ano = int(input("Digite o ano em que nasceu: "))

def MêsPorExtenso(dia, mes, ano):
    if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1:
        return f'\033[31mData Inválida\033[m!'
    else:
        stringMes = ''
        if mes == 1:
            stringMes = "Janeiro"
        elif mes == 2:
            stringMes = "Fevereiro"
        elif mes == 3:
            stringMes = "Março"
        elif mes == 4:
            stringMes = "Abril"
        elif mes == 5:
            stringMes = "Maio"
        elif mes == 6:
            stringMes = "Junho"
        elif mes == 7:
            stringMes = "Julho"
        elif mes == 8:
            stringMes = "Agosto"
        elif mes == 9:
            stringMes = "Setembro"
        elif mes == 10:
            stringMes = "Outubro"
        elif mes == 11:
            stringMes = "Novembro"
        else:
            stringMes = "Dezembro"
            
        stringAno = str(ano)
        if len(stringAno) == 4 or len(stringAno) > 4:
            returnAno = ano
        elif len(stringAno) == 3:
            returnAno = f"0{ano}"
        elif len(stringAno) == 2:
            returnAno = f"00{ano}"
        elif len(stringAno) == 1:
            returnAno = f"000{ano}"
           
            
        return f'{dia} de {stringMes} de {returnAno}'
    
print(MêsPorExtenso(Dia, Mês, Ano))