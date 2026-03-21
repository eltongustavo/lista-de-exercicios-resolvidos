atual = 0
proximo = 0
for x in range(0, 20):
    print(proximo, end=' ')
    proximo += atual
    atual = proximo - atual
    if proximo == 0:
        proximo += 1




