n = int(input('Enter number of students:'))
avg = 0

for i in range(1, n+1):
    print('Enter marks of Students', i)

    m1 = int(input('Subject 1:'))
    m2 = int(input('Subject 2:'))
    m3 = int(input('Subject 3:'))
    m4 = int(input('Subject 4:'))
    m5 = int(input('Subject 5:'))

    total = m1 + m2 + m3 + m4 + m5
    per = total / 5

    print('Percentange =', per)

    avg = avg + per

print('Average Percentage =', avg / n)    