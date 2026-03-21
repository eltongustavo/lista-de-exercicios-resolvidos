print("Comparador de Strings")
stringUm = input("Digite uma String: ")
stringDois = input("Digite outra String: ")

print()

print(f"O tamanho de '{stringUm}' é de: {len(stringUm)} caracteres")
print(f"O tamanho de '{stringDois}' é de: {len(stringDois)} caracteres")

print()

if len(stringUm) == len(stringDois):
    print("As duas Strings possuem o mesmo tamanho!")
else:
    print("As duas Strings não possuem o mesmo tamanho!")

if stringUm == stringDois:
    print("As duas Strings possuem o mesmo conteúdo!")
else:
    print("As duas Strings não possuem o mesmo conteúdo!")
