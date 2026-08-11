def palindrome(n):
    temp = n
    rev = 0

    while n > 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10

    if temp == rev:
        print('NUMBER IS PALINDROME')
    else:
        print('NUMBER IS NOT PALINDROME')

n = int(input('Enter number: '))

palindrome(n)