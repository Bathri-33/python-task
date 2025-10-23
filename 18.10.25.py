'''#1.check the key
a={23:"leo",4:"batman",58:103,22:"sanji"}
if in a:
    print("is already exit")
else:
    print("not exit")

#2 Merge two dictnory
a={23:"leo",4:"batman",58:103,22:"sanji"}
b={1:22,6:78}
a.update(b)
print(a) 

#3 sum of item
a={1:22,6:78,3:44,4:60}
b=sum(a.values())
print(b)'''

#4 iterte dict
a={23:"leo",4:"batman",58:103,22:"sanji"}
for key,value in a.items():
    print(f"Key:{key},value:{value}")

'''#5
a={x:x**2 for x in range(1,16)}
print(a)   

#6 remove a key
a={23:"leo",4:"batman",58:103,22:"sanji"}
a.pop(4)
print(a)

#7 length
a={23:"leo",4:"batman",58:103,22:"sanji"}
b=len(a)
print("the length of the dict is:",b)

#8 defalu key
a={23:"leo",4:"batman",58:103,22:"sanji"}
a.setdefault(2,"nill")
print(a)


#9 new dict from exixting dict
d={}
num=int(input("enter a count:"))
for i in range(num):
    key=input("enter the key value:")
    val=input("enter the value:")
    d[key]=val
print("dictinory:",d)
print(d.keys())
print()'''

#10 type of
d={}
num=int(input("enter a count:"))
for i in range(num):
    key=input("enter the key value:")
    val=input("enter the value:")
    d[key]=val
print("dictinory:",d)
print(type(key))
