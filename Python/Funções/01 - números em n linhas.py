def triangle_numbers(n):
    start = 1
    while start <= n:
        for x in range(0, start):
            print(start, end='   ')
        print()
        start += 1

triangle_numbers(6)