l1 = [10, 20, 30, 20, 40, 20, 50, 60]

n = int(input('Enter element to remove: '))

l2 = []

for i in l1:
    if i != n:
        l2.append(i)

print(l2)        