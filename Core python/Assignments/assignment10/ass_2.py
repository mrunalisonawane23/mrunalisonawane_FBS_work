l1 = [10, 20, 30, 40, 50, 60, 70]

max = l1[0]
min = l1[0]

for i in l1:
    if i > max:
        max = i

        if i < min:
            min = i

print('Maximum = ', max)
print('Minimum = ', min)
            