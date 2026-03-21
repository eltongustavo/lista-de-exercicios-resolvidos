peso_peixes = int(input('Digite o peso total de peixes pescados: '))
excesso = peso_peixes - 50
multa = 4 * excesso
print(f'Você pescou um total de {peso_peixes}kg de peixes, {excesso}kg acima do máximo permitido, a multa a ser paga é de {multa:.2f}R$')

