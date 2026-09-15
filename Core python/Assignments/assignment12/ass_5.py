str = input('Enter a string:')

print('Original String:', str)

count = 0

for ch in str:
    if ch in 'aeiouAEIOU':
        count = count + 1

print('Number of vowels in the string:', count)        