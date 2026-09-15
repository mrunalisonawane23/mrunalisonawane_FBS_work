l1 = [10, 20, 30, 20, 40, 30, 50, 20]

l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)        