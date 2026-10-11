length = float(input("Enter the length of a wall: "))
height = float(input("Enter the height of a wall: "))
rate = float(input("Enter painting cost per sq. meter: "))

area = 4 * length * height
total_cost = area * rate

print("Total area of four walls =", area, "sq. meters")
print("Total cost of painting = Rs.", total_cost)