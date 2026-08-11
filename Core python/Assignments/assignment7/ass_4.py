k = 4

for i in range(1, 6):

    for j in range(k):
        print(" ", end=" ")

    for j in range(i):
        print(i + j, end=" ")

    for j in range(i - 1):
        print(i + i - 2 - j, end=" ")

    k -= 1
    print()