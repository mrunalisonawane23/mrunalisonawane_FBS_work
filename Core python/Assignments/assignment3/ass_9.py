m1 = int(input('Enter Marks of Subject 1:'))
m2 = int(input('Enter Marks of Subject 2:'))
m3 = int(input('Enter Marks of Subject 3:'))
m4 = int(input('Enter Marks of Subject 4:'))
m5 = int(input('Enter Marks of Subject 5:'))

total = m1 + m2 + m3 + m4 + m5
per = total/5

if per >= 75:
    print('Distinction')
elif per >= 60:
    print('First class')
elif per >= 50:
    print('Second class')
elif per >=35:
    print('Pass')
else:
    print('Fail')    