gross_sales_sellers = []
while True:
    gross_sale = float(input('Digite o valor de vendas bruta do vendedor: (0 para finalizar)'))
    if gross_sale == 0:
        break
    gross_sales_sellers.append(gross_sale)

final_salary_sellers = []
for x in gross_sales_sellers:
    salary = 200 + (9 / 100 * x)
    final_salary_sellers.append(salary)

start = 200
end = 299

while True:
    contador = 0
    for x in final_salary_sellers:
        if start <= x <= end:
            contador += 1
    print(f'Existem {contador} vendedores ganhando entre R${start} e R${end}')
    start += 100
    end += 100
    if start == 1000:
        for x in final_salary_sellers:
            if x > start:
                contador += 1
        print(f'Existem {contador} vendedores ganhando mais de R${start}')
        break











