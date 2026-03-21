letra = str(input('Digite uma letra: ')).upper()[0]
if letra not in 'AEIOU':
    print(f'{letra} é uma consoante.')
else:
    print(f'{letra} é uma vogal.')