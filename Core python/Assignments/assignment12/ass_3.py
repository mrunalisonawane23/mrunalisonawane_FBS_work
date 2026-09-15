str1 = input('Enter first string: ')
str2 = input('Enter second string: ')

print('First String:', str1)
print('Second String:', str2)

if sorted(str1) == sorted(str2):
    print('The strings are Anagrams')
else:
    print('This strings are not Anagrams')    