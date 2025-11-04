# 1

class complexno:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complexno(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}"

c1 = complexno(3, 4)
c2 = complexno(5, 6)
result = c1 + c2
print("Result of addition:", result)

print("\n________****2****_________\n")

#2

def add(a, b, c=0):
    return a + b + c
print("Sum of two numbers:", add(2, 3))
print("Sum of three numbers:", add(2, 3, 4))


print("\n________****3****_________\n")

#3

class bird:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic bird sound")

class parrot(bird):
    def make_sound(self):
        print(f"{self.name} says: Squawk!")

class sparrow(bird):
    def make_sound(self):
        print(f"{self.name} says: Chirp Chirp!")

a1 = parrot("parrot")
a2 = sparrow("sparrow")

a1.make_sound()
a2.make_sound()


print("\n________****4****_________\n")


#4
class india:
    def __init__(self):
         self.ctry="india"
    def cap(self):
        print("capital of ",self.ctry,": New Delhi")
    def language(self):
        print("official language of",self.ctry,"no official language")
     


class USA:
    def __init__(self):
         self.ctry="USA"
    def cap(self):
        print("capital of  ",self.ctry,":washington")
    def language(self):
        print("official language of",self.ctry,"is american english")


class UK:
    def __init__(self):
         self.ctry="UK"
    def cap(self):
        print("capital of",self.ctry,":london")
    def language(self):
        print("official language of",self.ctry,"is british english")

obj1=india()
obj1.cap()
obj1.language()

print("\n_________________\n")

obj2=USA()
obj2.cap()
obj2.language()

print("\n_________________\n")

obj3=UK()
obj3.cap()
obj3.language()
