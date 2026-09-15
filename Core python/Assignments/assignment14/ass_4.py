l1 = [2, 4, 3, 5, 7, 8, 9]
value = 7

s1 = set(l1)

for i in s1:
    for j in s1:
        if i < j and i + j == value:
            print(i, j)