Palavra = input("Digite uma palavra: ")

def EmbaralhadorPalavras(palavra):
    import random;
    stringPalavra = str(palavra)
    listaLetras = []
    tamanhoPalavra = len(stringPalavra)
    for x in range(0, tamanhoPalavra):
        listaLetras.append(stringPalavra[x])
    random.shuffle(listaLetras)
    
    resultado = ''
    
    for x in listaLetras:
        resultado += x
        
    return resultado

print(EmbaralhadorPalavras(Palavra))
        
    
    
    