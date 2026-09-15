str = input('Enter a string: ')

words = str.split()
result = {}

for w in words:
    if w in result:
        result[w] = result[w] + 1
    else:
        result[w] = 1

print('Word Count:',result)            