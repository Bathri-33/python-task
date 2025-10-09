salary = int(input("Enter your salary: "))
print("salary:",salary)
service = int(input("Enter your years of service: "))
print("your sevice years:", service)
if service > 5:
    bonus = salary * 0.05
    print("You are eligible for a bonus of: ",bonus)
else:
    print("You are not eligible for a bonus.")
