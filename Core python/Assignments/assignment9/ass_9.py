def power(m, n):
    if(n > 0):
        return m * power(m, n - 1)
    else:
        return 1

m = 2
n = 5
res = power(m, n)
print(res)    