classes = int(input("Enter number of classes: "))
pres = int(input("Enter number of classes attended: "))

attendance = (pres / classes) * 100

print("Attendance Percentage:", attendance)

if attendance >= 50:
    print("Allowed to sit in exam")
else:
    print("Not Allowed to sit in exam")
