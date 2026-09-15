str = input('Enter a string: ')

di = {}

for word in str.split():
    if word in di:
        di[word] = di[word] + 1
    else:
        di[word] = 1

print(di)            