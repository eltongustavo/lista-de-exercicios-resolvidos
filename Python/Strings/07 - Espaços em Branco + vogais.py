frase = input("Digite uma string: ")
contadorVogais = 0
for x in range(0, len(frase)):
    if 'a' == frase[x].lower() or 'e' == frase[x].lower() or 'i' == frase[x].lower() or 'o' == frase[x].lower() or 'u' == frase[x].lower():
        contadorVogais += 1
        
contadorEspaçosEmBranco = frase.count(" ")

print(f"""A frase: {frase}\nPossui {contadorEspaçosEmBranco} espaços em branco\nE também possui {contadorVogais} vogais""")
