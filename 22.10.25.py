#1. find key
def stars(**a):
    for a in a.keys():
        print("key value",a)
stars(a=4,b=4,c=90)

#2 find value
def stars(**a):
    for a in a.values():
        print(" value",a)
stars(a=4,b=4,c=9)

#3 sum all num in list
def add(**a):
    sum=0
    for i in a.values():
        sum+=i
        print("sum is:",sum)
add(a=12,b=34,c=56)

#4 print even numbers
def bad(*a):
    for i in a:
        if i%2==0:
            i+=i+1
            print("the even nmbers are:",i,"/n")
bad(12,34,23,45) 

#5
def perfect_number(*a):
    for n in a:
        sum1=0
        for i in range(1,n):
            if n%i==0:
                sum1=sum1+i
        if sum1==n:
           print(n, "is a perfect num")
        else:
           print(n, "is not aperfect num")
perfect_number(6,28,12)
print()

#6 remove a last  key
def remove_last(**a):
    print("before remove:",a)
    a.popitem()
    print("after remove:",a)
remove_last(a=10,b=20,c=40,d=50)
print()

#7. Simple Calculator using Function
def calculator(a, b, op):
    if op == '+':
        print("Addition is:", a + b)
    elif op == '-':
        print("Subtraction is:", a - b)
    elif op == '*':
        print("Multiplication is:", a * b)
    elif op == '/':
        print("Division is:", a / b)
    else:
        print("Invalid operator")

calculator(10, 5, '+')
calculator(10, 5, '*')
print()

# 8. Check whether a passed string is palindrome or not
def palindrome(a):
    if a == a[::-1]:
        print(a, "is Palindrome")
    else:
        print(a, "is not Palindrome")

palindrome("madam")
palindrome("hello")
print()

# 9. Count number of vowels, consonant and special character in a string
def count_string(a):
    v = c = s = 0
    for ch in a:
        if ch.lower() in "aeiou":
            v = v + 1
        elif ch.isalpha():
            c = c + 1
        else:
            s = s + 1
    print("Vowels:", v)
    print("Consonants:", c)
    print("Special Characters:", s)

count_string("Hello@123")
