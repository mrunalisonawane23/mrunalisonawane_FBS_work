ch = 65

for i in range(1, 6):
    ch = 65
    for j in range(1, i + 1):
        print(chr(ch), end = ' ')
        ch = ch + 1
    print()    