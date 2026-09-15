l1 = [10, 20, 30, 20, 40, 10, 20, 30]

l2 = []

for i in l1:
    if i not in l2:
        count = 0
        for j in l1:
            if i == j:
                count = count + 1
        print(i, '=', count)
        l2.append(i)        