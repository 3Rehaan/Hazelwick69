grade = int(input("Please enter your test score"))
if grade < 0 or grade > 100:
    print("Error")
elif grade > 70:
    print("A")
elif grade > 60:
    print("B")
elif grade > 50:
    print("C")
elif grade > 40:
    print("D")
else:
    print("U")
