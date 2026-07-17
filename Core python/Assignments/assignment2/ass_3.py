feet = int(input("Enter distance in feet = "))
inch = int(input("Enter distance in inches = "))

total_inches = (feet * 12) + inch 
cm = total_inches * 2.54
m = cm / 100

print("Distance in meter =", m)
print("Distance in centimeter", cm)