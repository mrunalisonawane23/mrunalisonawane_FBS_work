import random
userId = input('Enter the user id =')
password = input('Enter the Password =')

if userId == 'admin' and password == 'samu@11':
    captcha = random.randint(1000,9999)
    print(f'Your Captcha ={captcha}')
    churser = int(input('Enter the Captcha = > '))
    if churser == captcha:
        print('Invalid Captcha.....')
    else:
        print('User is Invalid')    