n = int(input('Enter number of passenger:'))
cost = int(input('Enter ticket cost:'))

total = 0

for i in range(1, n + 1):
    age = int(input('Enter age of passenger: '))

    if age < 12:
        amt = cost - (cost * 30 / 100)
    elif age > 59: 
        amt = cost - (cost * 50 / 100)
    else:
        amt = cost 

        total = total + amt

print('Total Ticket Amount =', total)               