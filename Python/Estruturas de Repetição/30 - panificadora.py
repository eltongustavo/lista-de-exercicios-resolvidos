preço_pão = 0.18
print('Tabela de Preços Padaria:')
for x in range(1, 11):
    print(f'{f"{x:2}....R${preço_pão * x:.2f}":20} {f"{x+10}....R${preço_pão * (x+10):.2f}":20}'
          f'{f"{x+20}....R${preço_pão * (x+20):.2f}":20} {f"{x+30}....R${preço_pão * (x+30):.2f}":20}'
          f'{f"{x+40}....R${preço_pão * (x+40):.2f}":20}')


