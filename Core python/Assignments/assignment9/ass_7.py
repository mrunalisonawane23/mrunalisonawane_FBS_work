def sumdigit(n):
    if(n > 0):
        return n % 10 + sumdigit(n // 10)
    else:
        return 0

n = 12345
res = sumdigit(n)
print(res)    