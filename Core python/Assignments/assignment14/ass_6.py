l1 = [2, 5, 8, 10, 3, 7]

s1 = set(l1)

max_product = 0
pair = ()

for i in s1:
    for j in s1:
        if i < j:
            product = i * j

            if product > max_product:
                max_product = product
                pair = (i, j)

print(type(s1))
print('Pair:', pair)
print('Maximum product:', max_product)                