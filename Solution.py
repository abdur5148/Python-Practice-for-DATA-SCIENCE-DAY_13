print("For Deposit : D\nFor Withdrawal : W\nFor End Transaction : end\n")
var1 = 0
while True:
    a = input("Enter Transaction : ")
    if a.startswith("D"):
        var1 += int(a[2:])
    if a.startswith("W"):
        var1 -= int(a[2:])
    elif a == "end":
        break
print("Remaining Balance : ", var1)
