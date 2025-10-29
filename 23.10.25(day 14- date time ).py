'''from datetime import datetime as d
a=d.now()
b=a.timetuple()
print("current date time is",a)
print("current yeari",a.year)
print("month of the year is",a.month)
print("week num of the year",a.strftime("%U"))
print("week day of the week",a.strftime("%w"))
print("day of the year",a.strftime("%j"))
print("day of the month",b[2])
print("day of week",b[6])

#2 leap year
from datetime import datetime as d
d=int(input("enter a year"))
if d%4==0:
    print("it is leap year")
else:
    print("not a leap year")

#3 str to datetime

from datetime import datetime as d

x=int(input("Enter the date:"))
y=input("Enter the Month:")
z=int(input("Enter the year:"))

date=f"{x} {y} {z}"

print("Date",d.strptime(date,"%d %B %Y"))

#4
from datetime import datetime as d
x=d.now().time()
print("current time:",x)

#5
from datetime import datetime as d

smaple="June 6 2024 4:50AM"
print("convert datetime:",d.strptime(smaple,"%B %d %y %I:%M%p"))


#6
from datetime import datetime as d,timedelta
x=d.now()
z=x-timedelta(5)
z=x-timedelta(days=5)
print("current date:",x)
print("5days before:",z)

#7
from datetime import datetime as d,timedelta
x=d.now()
yesterday=x-timedelta(1)
tommorow=x+timedelta(1)
print("yesterday",yesterday)
print("tommrow",tommorow)

#8
from datetime import datetime as d,timedelta
x=d.strptime("28:33.0","%M:%S.%f")
add=x+timedelta(seconds=5)
print(add.strftime("%M:%S.%f")[::-3])

#9
from datetime import datetime as d
x=d.now()
print("current",x)
print("in milliseconds:",x.timestamp())

#10
from datetime import datetime as d
x=d.strptime("2015,6,16","%Y,%m,%d")
print("wek number:",x.strftime("%U"))

#11
from datetime import datetime as d
x=d(2025,9,6)
y=d(2003,9,6)
z=x-y
print("between days;",z)

#12
from datetime import datetime as d
d1=d(2025,10,28,0,0,0)
d2=d(2003,9,6,7,20,35)

diff=d1-d2

print("differnce",diff.days,"days",diff.seconds//3600,"hours",((diff.seconds//60)%60),"seconds")'''


#13
from datetime import date

def calculateage(dob):
    x=date.today()
    age=x.year-dob.year
    return age
dob=date(2003,9,6)
print("age:",calculateage(dob))
 


