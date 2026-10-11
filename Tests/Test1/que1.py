import math

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
r = float(input("Enter radius: "))

area = (l * b) + (0.5 * math.pi * r * r)
perimeter = (2 * l) + b + (math.pi * r)

print("Area =", area)
print("Perimeter =", perimeter)
