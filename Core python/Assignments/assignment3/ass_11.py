age1 = int(input('Enter the age of First person ='))
tkPrice1 = float(input('Enter the Ticket Price of First Person'))
totalPrice = 0
if age1 < 12:
    totalPrice = totalPrice + (tkPrice1 * 0.30)
elif age1 > 59:
    totalPrice = totalPrice + (tkPrice1 * 0.50)
else:
    totalPrice = totalPrice + tkPrice1
#first person ends here


age2 = int(input('Enter the age of Second person ='))
tkPrice2 = float(input('Enter the Ticket Price of Second Person'))

if age2 < 12:
    totalPrice = totalPrice + (tkPrice2 * 0.30)
elif age2 > 59:
    totalPrice = totalPrice + (tkPrice2 * 0.50)
else:
    totalPrice = totalPrice + tkPrice2
#Second person ends here


age3 = int(input('Enter the age of Third person ='))
tkPrice3 = float(input('Enter the Ticket Price of Third Person'))

if age3 < 12:
    totalPrice = totalPrice + (tkPrice3 * 0.30)
elif age3 > 59:
    totalPrice = totalPrice + (tkPrice3 * 0.50)
else:
    totalPrice = totalPrice + tkPrice3
#Third person ends here


age4 = int(input('Enter the age of Fourth person ='))
tkPrice4 = float(input('Enter the Ticket Price of Fourth Person'))

if age4 < 12:
    totalPrice = totalPrice + (tkPrice4 * 0.30)
elif age4 > 59:
    totalPrice = totalPrice + (tkPrice4 * 0.50)
else:
    totalPrice = totalPrice + tkPrice4
#Second person ends here


age5 = int(input('Enter the age of Fifth person ='))
tkPrice5 = float(input('Enter the Ticket Price of Fifth Person'))

if age5 < 12:
    totalPrice = totalPrice + (tkPrice5 * 0.30)
elif age5 > 59:
    totalPrice = totalPrice + (tkPrice5 * 0.50)
else:
    totalPrice = totalPrice + tkPrice5
#Second person ends here

print(f'Total price to pay for a Trip of Five people is {totalPrice}')







