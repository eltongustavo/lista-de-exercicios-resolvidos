def triangle_numbers(n):
    start = 1
    counter = 1
    while counter <= n:
        for x in range(start, counter + 1):
            print(x, end='   ')
        print()
        counter += 1

triangle_numbers(5)


