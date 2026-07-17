gender = input('Enter Gender (M/F):')
age = int(input('Enter Age:'))

if gender == "M" or gender == "m":
    if age >= 21:
        print('Eligible for Marriagle')
    else:
        print('Not Eligible for Marriage')
elif gender == "F" or gender == 'f':
    if age >= 18:
        print('Eligible for Marriage')
    else:
        print('Not Eligible for Marriage')
else:
    print('Invalid Gender')           