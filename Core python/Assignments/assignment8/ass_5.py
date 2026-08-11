def prime_sum(n):
    s = 0

    for i in range(2, n + 1):
        flag = 1

        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break

        if flag == 1:
            s = s + i

    print('SUM OF PRIME NUMBERS:', s)

n = int(input('Enter n: '))

prime_sum(n)

            
