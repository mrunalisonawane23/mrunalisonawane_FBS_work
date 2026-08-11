n = int(input('Enter the range:'))

print('Armstrong number are:')

for num in range(1, n + 1):
    temp = num
    sum = 0

    while temp > 0:
        rem = temp % 10
        sum = sum + (rem ** 3)
        temp = temp // 10

    if num == sum:
        print(sum)    