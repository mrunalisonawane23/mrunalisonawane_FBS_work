def reverse(n, rev):
    if(n > 0):
        return reverse(n // 10, rev * 10 + n % 10)
    else:
        return rev

n = 12345
res = reverse(n, 0)
print(res)     