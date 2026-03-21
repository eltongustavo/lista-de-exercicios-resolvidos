peso_clientes = []
altura_clientes = []
contador = 1
while True:
    peso = float(input(f'Digite o peso do cliente {contador}: (0 para finalizar) '))
    if peso == 0:
        if len(peso_clientes) == 0 or len(altura_clientes) == 0:
            print('Programa finalizado por falta de informações completa de pelo menos um cliente.')
            exit()
        else:
            break
    else:
        peso_clientes.append(peso)

    altura = float(input(f'Digite a altura do cliente {contador}: (0 para finalizar) '))
    print()
    if altura == 0:
        if len(peso_clientes) == 0 or len(altura_clientes) == 0:
            print('Programa finalizado por falta de informações completa de pelo menos um cliente.')
            exit()
        else:
            break
    else:
        altura_clientes.append(altura)
    contador += 1

media_peso_clientes = sum(peso_clientes) / len(peso_clientes)
media_altura_cliente = sum(altura_clientes) / len(altura_clientes)

cliente_mais_pesado = cliente_mais_leve = peso_clientes[0]
for x in peso_clientes:
    if x >= cliente_mais_pesado:
        cliente_mais_pesado = x
    elif x <= cliente_mais_leve:
        cliente_mais_leve = x


cliente_mais_alto = cliente_mais_baixo = altura_clientes[0]
for y in altura_clientes:
    if y >= cliente_mais_alto:
        cliente_mais_alto = y
    elif y <= cliente_mais_baixo:
        cliente_mais_baixo = y

print('='*60)
print(f'O maior peso entre os clientes foi de {cliente_mais_pesado}kg\n'
      f'O menor peso entre os clientes foi de {cliente_mais_leve}kg\n'
      f'A média de peso entre os clientes foi de {media_peso_clientes:.1f}kg\n')
print('='*60)
print(f'A maior altura entre os clientes foi de {cliente_mais_alto}m\n'
      f'A menor altura entre os clientes foi de {cliente_mais_baixo}m\n'
      f'A média de altura entre os clientes foi de {media_altura_cliente:.1f}m\n')
print('='*60)

