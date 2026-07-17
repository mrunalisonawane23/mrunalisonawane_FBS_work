import math

side = float(input("Enter Side:"))

#calculate area of equilateral triangle
area = (math.sqrt(3) / 4) * side * side

#display result
#print(area)
#print("Area of Equilateral Triangle:", area)
#print("Area of Equilateral Triangle is" + str(area))
print(f"Area of Equilateral Triangle with side {side} is {area}.")