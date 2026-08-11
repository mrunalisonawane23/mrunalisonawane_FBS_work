def armstrong(n):
    temp = n
    s = 0

    while n > 0:
        r = n % 10
        s = s + r ** 3
        n = n // 10

    if temp == s:
        print('NUMBER IS ARMSTRONG')
    else:
        print('NUMBER IS NOT ARMSTRONG')

n = int(input('Enter number: '))

armstrong(n)

