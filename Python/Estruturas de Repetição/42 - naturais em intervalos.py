entre_0_25 = []
entre_26_50 = []
entre_51_75 = []
entre_76_100 = []
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero < 0:
        break
    elif 0 <= numero <= 25:
        entre_0_25.append(numero)
    elif 26 <= numero <= 50:
        entre_26_50.append(numero)
    elif 51 <= numero <= 75:
        entre_51_75.append(numero)
    elif 76 <= numero <= 100:
        entre_76_100.append(numero)
    else:
        continue

print(f'Quantidade de números entre 0 e 25: {len(entre_0_25)} = {entre_0_25}')
print(f'Quantidade de números entre 26 e 50: {len(entre_26_50)} = {entre_26_50}')
print(f'Quantidade de números entre 51 e 75: {len(entre_51_75)} = {entre_51_75}')
print(f'Quantidade de números entre 76 e 100: {len(entre_76_100)} = {entre_76_100}')
