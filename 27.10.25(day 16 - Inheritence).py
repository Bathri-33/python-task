#1,
class personal:
    def name(self):
        return "badri"
    def email(self):
        print("nanthandaleo@gmail.com")
    def mobile(self):
        print("7708238868")
    def address(self):
        print("madurai")
class educational(personal):
    def bsc(self):
        print("Bsc Computer Science")
a=educational();
a.bsc()
print()

#2,
class personal:
    def name(self):
        print("badri")
    def email(self):
        print("nathandaleo@gmail.com")
    def mobile(self):
        print("7708238868")
    def address(self):
        print("madurai")
class educational(personal):
    def bsc(self):
        print("Bsc Computer Science")
class bank(educational):
    def account(self):
        print("HDFC Bank")
    def no(self):
        print("2368339273")
        
a=bank()
a.name()
a.email()
a.address()
a.account()
a.no()
print()

#3,
class school:
    def name1(self):
        print("nader school")
    def email1(self):
        print("naderschoolgmail.com")
    def mobile1(self):
        print("7708238868")
    def address1(self):
        print("kariapatti")
class staff(school):
    def name2(self):
        print("vasanthi tamil teacher for 6 to 10")
    def mail2(self):
        print("jvasu@gmail.com")
    def mobile2(self):
        print("95875878488")
    def address2(self):
        print("kariapatti")
    def dep2(self):
        print("Tamil Teacher")
class student(school):
    def name3(self):
        print("badri")
    def Class3(self):
        print("10th class c")
a=student()
b=staff()
a.name3()
a.mobile1()
b.name2()


