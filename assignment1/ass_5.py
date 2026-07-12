P = int(input("Enter principal amount:"))
R = float(input("Enter Rate of Interest:"))
T = int(input("Enter Time in years:"))

#calculate compound amount and compound interest
A =  P * (1 + R / 100) ** T
CI = A - P

#display result
#print(CI)
#print("Compound Interest:", CI)
#print("Compound Interest is " + str(CI))
print(f"Compound Interest for Principal {P}, Rate {R}% and Time {T} years is {CI}.")