l1 = [10, 20, 30, 40, 50, 60]
l2 = [30, 40, 50, 60, 70, 80]

l3 = []

for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            l3.append(l1[i])

print('Intersection of two lists =', l3)            