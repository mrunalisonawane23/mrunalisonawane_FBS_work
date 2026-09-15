l1 = [10, 20, 30, 40, 50, 60]

for i in range(len(l1)):
    for j in range(len(l1) - 1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]

print('Sorted list =', l1)
print('Second largest number =', l1[-2])            

             