l1 = [1, 2, 3, 4, 5]
l2 = []
l3 = []

for i in range(len(l1)):
    l2.append(l1[i] ** 2)
    l3.append(l1[i] ** 3)

print('List of numbers =', l1)
print('List of sqaures =', l2)
print('List of cubes =', l3)