import math

radius = float(input("Enter Radius:"))

#calculate area and circumference
area = math.pi * radius * radius
circumference = 2 * math.pi * radius

#display result
#print(area)
#print(circumference)
#print("Area of Circle:", area)
#print("Circumference of Circle:", circumference)
#print("Area of Circle is" + str (area))
#print("Circumference of Circle is" + str(circumference))
#print(f"Area of Circle with radius {radius} is {area}.")
print(f"Circumference of Circle with radius {radius} is {circumference}")