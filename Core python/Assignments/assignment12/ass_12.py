str = input('Enter a string: ')

count = 0
for ch in str:
    if ch.islower():
        count = count + 1

print('Number of Lowercase characters:', count)        