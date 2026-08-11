#a. 1+2+3+....+n
def series(n):
    s = 0

    for i in range(1, n + 1):
        s = s + i

    print('SUM = ', s)

n = int(input('Enter n: '))

series(n)

#b. 1!+2!+3!+....+n!
def series(n):
    s = 0

    for i in range(1, n + 1):
        f = 1
        for j in range(1, i + 1):
            f = f * j
        s = s + f 

    print('SUM =', s)

n = int(input('Enter n: '))

series(n)

#c. 1^1+2^2+3^3+.....+n^n
def series(n):
    s = 0

    for i in range(1, n + 1):
        s = s + i ** i

    print('SUM =', s)

n = int(input('Enter n: '))

series(n)

