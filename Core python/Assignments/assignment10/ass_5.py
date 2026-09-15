l1 = [10, 20, 30, 20, 40, 20, 50, 60]

n = int(input('Enter number: '))

count = 0

for i in l1:
    if i == n:
        count = count + 1

if count > 0:
    print('Element is present')
    print('count =', count)
else:
    print('Element is not present')    
