str = input('Enter a string: ')

print('Original String:', str)

new_str = str[-1] + str[1:-1] + str[0]

print('String after exchanging first and last character:', new_str)