l1 = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

s1 = set(l1)

groups = {}

for word in s1:
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print(type(s1))
print(groups)        