a=int(input("enter the lengh:"))
b=int(input("enter the breath:"))
c=int(input("enter the height:"))
if a == b and a == c:
    print("the triangle is equilateral")
elif a == b or b== c:
    print("the triangle is  isoceles")
else:
    print("the triangle is scalen")
    
