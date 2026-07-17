num = int(input('Enter number:'))

if(num > 0):
    if(num > 50):
        if(num > 100):
            if(num > 150):
                if(num > 250):
                    print('The number is greater than 250')
                else:
                    print('150-250')
            else:
                print('100-150')
        else:
            print('50-100')
    else:
        print('0-50')
else:
    print('The number is greater than 0')                                   

