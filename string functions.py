'''#8,
name=input("enter a string:")
print("index of first a:",name.index('a'))
print()


#9,
a=input("enter a string")
if a.isalpha():
    print("alph")
else:
    print("not alpha")'''


#10
a=input("enter a string")
reverse=""
for char in a:
    reverse=char+reverse
print(reverse)
print()
