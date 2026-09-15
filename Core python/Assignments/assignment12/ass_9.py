str = input('Enter a string: ')

words = str.split()
word_count = len(words)

char_count = len(str.replace(' ', ''))

print('Number of words:', word_count)
print('Number of Charaters:', char_count)