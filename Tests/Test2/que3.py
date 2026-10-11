import math

r = 20
l = 50
b = 40
cost = 35

# Perimeter of half circle
semi_circle = math.pi * r

# Perimeter of rectangle
rectangle = 2 * (l + b)

# Total perimeter of the field
perimeter = semi_circle + rectangle

# Fencing 5 times
total_wire = perimeter * 5

# Total cost
total_cost = total_wire * cost

print("Total wire required:", total_wire, "m")
print("Total cost of fencing: Rs.", total_cost)