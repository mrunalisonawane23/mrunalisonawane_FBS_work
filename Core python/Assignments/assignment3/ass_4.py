a = int(input('Enter First Side:'))
b = int(input('Enter Second Side:'))
c = int(input('Enter Third Side:'))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('Triangle is valid')
else:
    print('Triangle is not valid')    