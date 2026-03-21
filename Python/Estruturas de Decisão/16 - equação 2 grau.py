a = float(input('Digite o valor de "a": '))
if a == 0:
    print('Não existe raiz quadrada com "a" = 0')
    exit()

b = float(input('Digite o valor de "b": '))
c = float(input('Digite o valor de "c": '))

delta = (b**2) - 4 * a * c

if delta < 0:
    print('Não existes raízes quadradas com delta negativo.')
    exit()

if delta == 0:
    print('Com delta nulo, a raiz quadrada só possui uma solução : ', end='')
    raiz = (-b + delta**(1/2)) / (2*a)
    print(f'{raiz:.2f}')
    print()
elif delta > 0:
    print('Com delta positivo, a raiz quadrada possui duas raízes: ', end='')
    raiz_um = (-b + delta**(1/2)) / (2*a)
    raiz_dois = (-b - delta**(1/2)) / (2*a)
    print(f'{raiz_um:.2f} e {raiz_dois:.2f}')

