l1 = [10, 20, 30, 40, 50, 60, 70]

largest = l1[0]
second = l1[0]

for i in l1:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i !=largest:
        second = i

print('Second largest =', second)        
    
