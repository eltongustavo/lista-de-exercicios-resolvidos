pais_a = 8000
pais_b = 20000
contador_anos = 0
while pais_a < pais_b:
    pais_a += (3 / 100 * pais_a)
    pais_b += (1.5 / 100 * pais_b)
    contador_anos += 1
print(f'Serão necessários {contador_anos} anos para a população do país A igualar ou superar o país B.')


