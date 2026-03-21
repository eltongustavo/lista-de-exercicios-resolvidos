anterior = 0
proximo = 0
while proximo < 500:
    print(proximo, end=' ')
    proximo += anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo += 1
print(proximo)
