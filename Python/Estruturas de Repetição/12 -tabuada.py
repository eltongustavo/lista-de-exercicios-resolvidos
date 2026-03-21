multiplication_table_num = int(input('Enter a number that you want to see the multiplication table: '))
for x in range(1, 11):
    print(f'{multiplication_table_num} x {x:2} = {multiplication_table_num * x}')