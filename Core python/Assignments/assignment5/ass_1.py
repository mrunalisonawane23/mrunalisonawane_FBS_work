userid = 'admin'
password = '1234'

for i in range(1, 4):
    uid = input('Enter User ID:')
    pwd = input('Enter Password:')

    if uid == userid and pwd == password:
        print('Login Successful')
        break
    else:
        print('Invalid user ID or Password')

if uid != userid or pwd != password:
    print('Program Terminated')        