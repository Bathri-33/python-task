'#1. creat a list of furit and print
a=[]
for i in range(5):
    b=input("enter a fuirt:")
    a.append(b)
print(a)
    
#2.add and remove furit
a=["apple","orange","grape"]
a.append("guva")
a.remove("apple")
print(a)

#3.find max and min
a=[1,3,56,78,13,99]
b=max(a)
print("the max value:",b)
c=min(a)
print("the min value:",c)

#4.sort the list
a=[23,4,6,19,42]
a.sort()
print(a)

#5.join 2 list
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

#6.print all item of a list
a=[]
count=int(input("enter num of cities"))
for i in range(count):
    b=input("enter the cities:")
    a.append(b)
print(a)

#7.sum of the list
a=[12,3,4,6]
sum=0
for i in a:
    sum+=i
print(sum)

#8.count no of even number
a=[1,2,3,4,5,6,7,8]
count=0
for i in a:
    if i%2==0:
        count+=1
print(count)'''

#9. square of list
a=[1,2,3,4,5]

print(b)


