ch = 65

for i in range(1, 6):

    for j in range(1, 6 - i):
        print(' ', end = ' ')

    ch = 65
    for j in range(1, 2 * i):
        print(chr(ch), end = ' ')
        ch = ch + 1 

    print()       