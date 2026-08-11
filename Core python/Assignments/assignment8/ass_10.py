def leap_year(year):
    if year % 400 == 0:
        print('YEAR IS LEAP YEAR')
    elif year % 100 == 0:
        print('YEAR IS NOT LEAP YEAR') 
    elif year % 4 == 0:
        print('YEAR IS LEAP YEAR')
    else:
        print('YEAR IS NOT LEAP YEAR')

y = int(input('Enter year: '))

leap_year(y)