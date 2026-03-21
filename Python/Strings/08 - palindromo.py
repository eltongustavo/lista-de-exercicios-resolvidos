frase = input("Digite algo para verificar se é um palindromo: ").strip().split()
resultado = ''
for x in range(0, len(frase)):
    resultado += frase[x]
if resultado[::].upper() == resultado[::-1].upper():
    print(f'{resultado[::-1].upper()} é um palindromo de {resultado[::].upper()}')
else:
    print(f'{resultado[::-1].upper()} não é um palindromo de {resultado[::].upper()}')

