P = int(input("Enter principal amount:"))
R = float(input("Enter Rate of Interest:"))
T = int(input("Enter Time in years:"))

#perform calculation
SI = (P * R * T) / 100

#display result
#print(SI)
#print("Simple Interest:", SI)
#print("Simple Interest is " + str(SI))
print(f"Simple Interest for Pricipal {P}, Rate {R}% and Time {T} years is {SI}.")