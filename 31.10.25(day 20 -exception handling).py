'''#1
try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("enter a value above 0")
except ValueError:
    print("enter the valid input")




print("\n____________*****_____________\n")

#2

try:
    a=int(input("enter a number:"))
    b=input("enter a number:") 
    c=a+b
    print(c)
except TypeError:
    print("both are different type")
except ValueError:
    print("enter the valid input")



print("\n____________*****_____________\n")

#3


try:
    a=int(input("Enter a number:"))
    print("valid integer",a)

except ValueError as n:
    print("value error",n)


print("\n____________*****_____________\n")

#4


try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs must be numerical.")
    print("Valid numbers entered:", float(a), float(b))
except TypeError as e:
    print("TypeError:", e)

print("\n____________*****_____________\n")


#5. 

try:
    lst = [10, 20, 30, 40, 50]
    value = int(input("Enter value to search: "))
    if value not in lst:
        raise ValueError(f"{value} not found in the list")
    print(f"{value} found at index {lst.index(value)}")
except ValueError as e:
    print("Error:", e)


print("\n____________*****_____________\n")'''


#6.

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


from datetime import date, timedelta

def today_date():
    d = date.today()
    return d.strftime("%d %B %Y, %A")

def yesterday():
    d = date.today() - timedelta(days=1)
    return d.strftime("%d %B %Y, %A")

def tomorrow():
    d = date.today() + timedelta(days=1)
    return d.strftime("%d %B %Y, %A")

import simple_calc
import date_today

try:
    a = float(input("Enter the A Value: "))
    b = float(input("Enter the B Value: "))

    print("1. Addition  2. Subtraction  3. Multiplication  4. Division")
    choice = int(input("Enter the choice to perform: "))

    print("\nDate:", date_today.today_date())

    if choice == 1:
        print("Addition of Two numbers:", simple_calc.add(a, b))
    elif choice == 2:
        print("Subtraction of Two numbers:", simple_calc.sub(a, b))
    elif choice == 3:
        print("Multiplication of Two numbers:", simple_calc.mul(a, b))
    elif choice == 4:
        print("Division of Two numbers:", simple_calc.div(a, b))
    else:
        print("Invalid choice.")

except ZeroDivisionError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter numeric input only.")
else:
    print("Calculation completed successfully.")
finally:
    print("Program ended.")
