#1!+2!+3!+4!+.....+n!
def fact(n):
    if(n > 0):
        return n * fact(n - 1)
    else:
        return 1

def series(n):
    if(n > 0):
        return fact(n) + series(n - 1)
    else:
        return 0

n = 5
res = series(n)
print(res)        