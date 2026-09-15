n = 1

for i in range(10):
    l = []
    for j in range(10):
        l.append(n)
        n = n + 1

    if i % 2 != 0:
        l.reverse()

    print(l)        