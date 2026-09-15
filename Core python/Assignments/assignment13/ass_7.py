di = {1: 'Python', 2: 'Java', 3: 'C++', 4: 'JavaScript'}

key = int(input('Enter key to remove: '))

if key in di:
    del di[key]
    print(di)
else:
    print('Key does not exists')    