#1
class Student:
    def __init__(self, name):
        self.__name = name  
        self.__grades = []

    def add_grade(self, grade):
        self.__grades.append(grade)

    def get_average(self):
        if len(self.__grades) == 0:
            return 0  
        return sum(self.__grades) / len(self.__grades)

    def get_name(self):
        return self.__name


student = Student("parthipan")
student.add_grade(85)
student.add_grade(56)
print(student.get_average())
print(student.get_name())   


print("\n_______****2****________\n")

#2
class employee:
    def __init__(self,name):
        self.__name=name
        self.__salary=float
    def set_salary(self,amount):
        if amount >0:
             self.__salary =amount
        else:
              print("invalid salary amount")

    def get_salary(self):
        return self.__salary

    def get_name(self):
        return self.__name        

emp = employee("Bob")
emp.set_salary(5000)
print(emp.get_salary())
emp.set_salary(-100) 
print(emp.get_name()) 
         
