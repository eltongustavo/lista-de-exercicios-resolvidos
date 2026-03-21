pais_a = int(input('Digite a população do país A: '))
crescimento_A = float(input('Digite a taxa de crescimento anual da população do país A(em %): '))

pais_b = int(input('Digite a população do país B: '))
crescimento_B = float(input('Digite a taxa de crescimento anual da população do país B(em %): '))

if pais_a > pais_b:
    maior = pais_a
    maior_aux = 'A'
    menor = pais_b
    menor_aux = 'B'
    crescimento_maior = crescimento_A
    crescimento_menor = crescimento_B
else:
    maior = pais_b
    maior_aux = 'B'
    menor = pais_a
    menor_aux = 'A'
    crescimento_maior = pais_b
    crescimento_menor = pais_a


contador_anos = 0

while menor < maior:
    menor += (crescimento_menor / 100 * menor)
    maior += (crescimento_maior / 100 * maior)
    contador_anos += 1

print(f'Para o país menor {menor_aux} supere o país maior {maior_aux}, levará cerca de {contador_anos} anos.')
