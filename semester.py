year=int(input("enter the year(1-3):"))
sem=int(input("enter the sem(1-6):"))

if year==1:
    if sem==1:
        print("tamil \n english \n differntial \n inegeratiom \n ")
    elif sem==2:
        print("tmail2 \n  english2 \n  set \n  group ")
    else:
        print("invaild year")
elif year==2:
    if sem==3:
        print("tamil \n english \n ring \n statistic \n ")
    elif sem==4:
        print("tamil \n english \n ring opp \n numeric \n ")
    else:
        print("invaild year")


elif year==3:
    if sem==5:
        print("differntial calculas \n field \n ")
    elif sem==6:
        print(" analyis complex analysis \n ")
    else:
        print("invaild year")


else:
    print("not in clg")
