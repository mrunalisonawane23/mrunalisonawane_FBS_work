k = 4

for i in range(k):
    num = 1
    print(' '*(k-i-1), end = ' ')
    for j in range(i + 1):
        print(num, end = ' ')
        num = num*(i - j) // (j + 1)
    print()  