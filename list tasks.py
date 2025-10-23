'''name=[]
count=int(input("no of nums"))
for c in range(count):
    values=input("enter a num")
    name.append(values)
print(name)

#2
a=["apple","orange","grape","guva"]
a.append("dragon furit")
a.remove("apple")
print(a)

#3
a=["apple","orange","grape","guva"]
for i in a:
    print(i)


#4
a=[1,2,3,4]
for i in range(5,7):
    a.append(i)
print(a)

#5-remove city
city=["Madurai","coimbatore","thircy","nellai","erode"]
city.remove("nellai")
print(city)

    
#6.Delete last element
a=[12,34,56,777,8.9]
a.pop()
print(a)

#7.add sub to list
a=[]
for i in range(5):
    b=input("enter the sub:")
    a.append(b)
print(a)

#8.remove specific item
a=[12,"badri",45,"jjk","op",6578]
b=input("enter the item to be removed:")
a.remove(b)
print(a)

#9.add num 1 to 10 using for loop
a=[]
for i in range(1,11):
    a.append(i)
print(a)'''

#10.remove all even num
a=[1,2,6,7,9,8,29,54,77]
for i in a:
    if i%2==0:
        a.remove(i)
print(a)




