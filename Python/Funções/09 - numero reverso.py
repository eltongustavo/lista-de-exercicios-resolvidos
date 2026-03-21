numero = int(input("Digite um número: "))

def NumeroReverso(num):
    stringNum = str(num)
    stringReversa = ''.join(reversed(stringNum))
    numInvertido = int(stringReversa)
    return f'O número {num} ao contrário fica {numInvertido}'
    
print(NumeroReverso(numero))
    
    