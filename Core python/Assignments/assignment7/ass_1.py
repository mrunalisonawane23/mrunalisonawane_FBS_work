n = 5
k = -1

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(' ', end=' ')
    print('*', end=' ')

    if i != 1:
        k += 2
        for j in range(1, k + 1):
            print(' ', end=' ')
        print('*', end=' ')
    print()

for i in range(n, 0, -1):
    for j in range(1, n - i + 1):
        print(' ', end=' ')
    print('*', end=' ')

    if i != 1:
        for j in range(1, k + 1):
            print(' ', end=' ')
        print('*', end=' ')
        k -= 2
    print()
