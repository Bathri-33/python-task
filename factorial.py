a=int(input("enter a num:"))
fact=1
if a<0:
    print("invalid")
elif n==1:
    print("the fact of 0 is 1")
else:
    for i in range (1,a+1):
        fact *= i
        print("the factorial of",a,"is",fact)
    
    
