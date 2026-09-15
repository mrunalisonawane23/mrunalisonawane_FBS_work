str1 = input('Enter first string: ')
str2 = input('Enter second string: ')

len1 = 0
for ch in str1:
    len1 = len1 + 1

len2 = 0
for ch in str2:
    len2 = len2 + 1

if len1 > len2:
    print('Larger String:', str1)
else:
    print('Larger String:', str2)            