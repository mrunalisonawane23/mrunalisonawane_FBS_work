def odd_sum(n):
    s = 0

    for i in range(1, n + 1, 2):
        s = s + i

    print('SUM OF ODD NUMBERS:', s)

n = int(input('Enter n: '))

odd_sum(n)