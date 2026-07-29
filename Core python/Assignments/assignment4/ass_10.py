n = int(input('Enter number:'))
sum = 0
for i in range(1, n):
    if n %1 == 0:
        sum = sum + i
if(n == sum):
    print('Perfect number.')
else:
    print('Not Perfect number.')    
