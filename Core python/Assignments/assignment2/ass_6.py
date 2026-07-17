basic = int(input("Enter basic salary = "))
 
da = basic * 10 / 100
ta = basic * 12 / 100
hra = basic * 15 / 100

total = basic + da + ta + hra

print("DA =", da)
print("TA =", ta)
print("HRA =", hra)
print("Total Salary =", total)