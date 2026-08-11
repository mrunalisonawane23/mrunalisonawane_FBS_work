def armstrong(n, p):
    if(n > 0):
        return (n % 10) ** p + armstrong(n // 10, p)
    else:
        return 0

n = 153
p = len(str(n))
res = armstrong(n, p)

if(res == n):
    print('Armstrong number')
else:
    print('Not Armstrong number')    