ten_characters = []
for _ in range(1, 11):
    ten_characters.append(str(input(f'Digite o caractere {_}: ')))

counter_consonants = 0

for y in ten_characters:
    if y not in 'aeiouAEIOU':
        counter_consonants += 1


print(f'Nos 10 caracteres analisados, foram encontrados {counter_consonants} consoantes/números.')
for x in ten_characters:
     if x not in 'aeiouAEIOU':
         print(x, end=' ')




