l1 = [10, 20, 31, 40, 51, 60, 70]

even = []
odd = []

for i in l1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print('Even list =', even)
print('Odd list =', odd)            