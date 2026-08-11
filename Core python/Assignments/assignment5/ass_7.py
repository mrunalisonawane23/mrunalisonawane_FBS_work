#a: 1! = 2! = 3! +...n!
n = int(input('Enter value of n:'))
sum = 0

for i in range(1, n + 1):
    fact = 1

    for j in range(1, i + 1):
        fact = fact * j
        sum = sum + fact
print('sum =', sum)  

#b: N + N^2 + N^3 +....+N^N  
n = int(input('Enter value of n:'))

sum = 0

for i in range(1, n + 1):
    sum = sum + (n ** i)

print('Sum =', sum) 
 
#c: sum of geometric series 
n = int(input('Enter value of n:'))

sum = 0
term = 1

for i in range(1, n + 1):
    sum = sum + term
    term = term * 2

print('Sum =', sum)    

#d: S = a + a^2/2+a^3/3+....+a^10/10  
a = int(input('Enter value of a:'))

sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print('Sum =', sum)  

#e: x-x^2/3+x^3/5-x^4/7+....n terms     
x = int(input('Enter value of x:'))
n = int(input('Enter number of terms:'))

sum = 0
sign = 1
d = 1

for i in range(1, n + 1):
    sum = sum + sign * (x ** i) / d
    sign = sign * (-1)
    d = d + 2

print('Sum =', sum) 
