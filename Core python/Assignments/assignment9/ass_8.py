def prime(n, i):
    if(i == 1):
        return True
    elif(n % i == 0):
        return False
    else:
        return prime(n, i - 1)

n = 17
res = prime(n, n - 1)

if(res):
    print('Prime number')
else:
    print('Not Prime number')    