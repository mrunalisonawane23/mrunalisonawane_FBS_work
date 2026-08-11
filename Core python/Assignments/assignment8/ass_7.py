def sum_digit(n):
    s = 0

    while n > 0:
        r = n % 10
        s = s + r
        n = n // 10

    print('SUM OF DIGITS:', s)

n = int(input('Enter number: '))

sum_digit(n)
