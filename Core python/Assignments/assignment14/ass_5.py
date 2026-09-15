l1 = ['flower', 'flow', 'flight']

s1 = set(l1)

prefix = ''

for i in range(len(l1[0])):
    ch = l1[0][i]

    if all(word[i] ==  ch for word in s1 if i < len(word)):
        prefix = prefix + ch 
    else:
        break

print(type(s1))
print('Longest common prefix:', prefix)        