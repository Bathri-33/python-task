'''#1
from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class lion(animal):
    def sound(self):
        print("lion:na tha da leo")


class tiger(animal):
    def sound(self):
        print("tiger:RAAAAAAAAATAAAA")


leo=lion()
puli=tiger()

leo.sound()
puli.sound()


print("\n________****2****______\n")'''


#2
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass

    @abstractmethod
    def calculatemeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius * self.radius

    def calculatemeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculateArea(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def calculatemeter(self):
        return self.a + self.b + self.c


circle = Circle(5)
triangle = Triangle(3, 4, 5)

print("Circle Area:", circle.calculateArea())
print("Circle Perimeter:", circle.calculatemeter())
print("Triangle Area:", triangle.calculateArea())
print("Triangle Perimeter:", triangle.calculatemeter())


print("\n________****3****______\n")


'''#3
from abc import ABC, abstractmethod
import math

class Shapes(ABC):
    @abstractmethod
    def volume(self):
        pass


class Cylinder(Shapes):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius * self.radius * self.height

class Cone(Shapes):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return (1/3) * math.pi * self.radius * self.radius * self.height



class Sphere(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3


cylinder = Cylinder(3, 7)
cone = Cone(3, 7)
sphere = Sphere(3)

print("Cylinder Volume:", cylinder.volume())
print("Cone Volume:", cone.volume())
print("Sphere Volume:", sphere.volume())'''

