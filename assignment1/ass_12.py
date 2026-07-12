import math

radius = float(input("Enter Radius:"))

#calculate volume of sphere
volume = (4 / 3) * math.pi * radius * radius *radius

#display result
#print(volume)
#print("Volume of Sphere:", volume)
#print("Volume of Sphere is" +  str(volume))
print(f"Volume of Sphere with radius {radius} is {volume}.")