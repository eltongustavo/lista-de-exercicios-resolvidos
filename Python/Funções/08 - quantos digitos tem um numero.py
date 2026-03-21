Linhas = int(input("Digite a quantidade de Linhas: "))
Colunas = int(input("Digite a quantidade de Colunas: "))

def Moldura(linhas=1, colunas=1):
    quantidadeLinhas = int(linhas)
    quantidadeColunas = int(colunas)
    
    resultado = """"""
    multColunas = int(colunas) - 2
    resultado += '+' + ('-'*multColunas) + '+\n'
    for x in range(0, linhas-2):
        resultado += "|" + (" "*multColunas) + "|\n"
    resultado += '+' + ('-'*multColunas) + '+'
    
    return resultado

print(Moldura(Linhas, Colunas))   
