l1 = ['apple', 'banana', 'apple', 'mango', 'banana', 'apple']

s1 = set(l1)

print(type(s1))
print('Unique words:', s1)

for word in s1:
    print(word, ':', l1.count(word))