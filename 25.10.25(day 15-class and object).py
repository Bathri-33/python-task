#1,
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

r = float(input("Enter radius of circle: "))
c = Circle(r)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

#2,
from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # format YYYY-MM-DD

    def age(self):
        birth = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age

name = input("Enter name: ")
country = input("Enter country: ")
dob = input("Enter date of birth (YYYY-MM-DD): ")
p = Person(name, country, dob)
print(p.name, "is", p.age(), "years old")

#3,
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero not allowed"

calc = Calculator()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", calc.add(a, b))
print("Subtraction:", calc.sub(a, b))
print("Multiplication:", calc.mul(a, b))
print("Division:", calc.div(a, b))

#4,
import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

c = Circle(5)
s = Square(4)
t = Triangle(3, 4, 5)

print("Circle - Area:", c.area(), "Perimeter:", c.perimeter())
print("Square - Area:", s.area(), "Perimeter:", s.perimeter())
print("Triangle - Area:", t.area(), "Perimeter:", t.perimeter())








