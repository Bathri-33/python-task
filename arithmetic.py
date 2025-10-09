a=int(input("enter a value:"))
b=int(input("enter a value:"))
print("1.add \n")
print("2.sub \n")
print("3.mult \n")
print("4.div \n")

c=int(input("enter yor choice (1-4):"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
else:
    print("invalid")
    
    
