import math

a = float(input("Enter value of a:"))
b = float(input("Enter value of b:"))
c = float(input("Enter value of c:"))

#Calculate discriminant
d = (b * b) - (4 * a * c)

#calculate roots
root1 = (-b + math.sqrt(d)) / (2 * a)
root2 = (-b + math.sqrt(d)) / (2 * a)

#display result
print(root1)
print(root2)
print("First Root:", root1)
print("Second root:", root2)
print("First Root is " + str(root1))
print("Second Root is " + str(root2))
print(f"Roots of the quadratic equation are {root1} and {root2}.")