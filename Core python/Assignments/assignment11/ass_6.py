l1 = [10, 20, 30, 40, 50, 60]
l2 = [30, 40, 50, 60, 70, 80]

for i in range(len(l2)):
    if l2[i] not in l1:
        l1.append(l2[i])

print('Union of two lists =', l1)        