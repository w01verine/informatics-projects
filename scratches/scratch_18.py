mygrade = int(input("Enter Test Score: "))

if mygrade < 50:
    print("F")
elif mygrade < 60:
    print("D")
elif mygrade < 75:
    print("C")
elif mygrade < 85:
    print("B")
elif mygrade <= 100:
    print("A")
else:
    print("Invalid Grade")

