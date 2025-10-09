apti = float(input("Enter marks in Aptitude: "))
gd = float(input("Enter marks in GD: "))
tech = float(input("Enter marks in Technical: "))
hr = float(input("Enter marks in HR: "))


if apti >=85 and  gd  >=90 and tech >=80 and hr >=95:
    total = apti+ gd + tech+ hr
    
    if total >390 and total <=400:
        salary = 30000
    elif  total >=380 and total <=390:
        salary = 28000
    elif total >=370 and total <=380:
        salary = 25000
    elif total >=350 and total <=370:
        salary = 20000
    else:
        salary = 0  
    
    if salary > 0:
        print(" Candidate is Eligible for the Job.")
        print("Total Marks:",total)
        print("Salary Offered: ",salary)
    else:
        print(" Eligible but marks not sufficient for salary consideration.")
else:
    print("Candidate is NOT Eligible for the Job.")
