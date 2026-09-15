l1 = [2, 3, 4, 5, 6, 7]
target = 12

s1 = set(l1)

for i in s1:
    for j in s1:
        for k in s1:
            if i < j < k and i + j + k == target:
                print(i, j, k)