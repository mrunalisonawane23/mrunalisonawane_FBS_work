n = int(input('Enter number:'))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    temp = temp // 10 

if sum == n:
    print('Strong number')
else:
    print('Not a String number')           