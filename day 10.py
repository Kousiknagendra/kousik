#) Tasks


#Write the code for the belwo tasks using function
#1.) d1 = {"shirt": 1000, "pant"; 1500, "Shoes"; "900", "handkey": 30}
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 'S'

#2.) Find then 67, is strong number or not

#3.) 11 = [1,2,3,4,5,6]
#n=2--> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]

#-------------------------------------------------------------------------------#

# ! Method riding
# polymorphism in classes uisng Inheritence
'''
class bank:
    def ratio(self):
        print("All bamks has repo rete")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()

IOB rate is 7.5%
SBI rate is 9%
'''

# Eg:2

'''
class USA:
    def language(self):
        print("English")

    def capital(self):
        print("Washington DC")

class India(USA):
    def language(self):
        print("None")

    def capital(self):
        print("New Delhi")

I = India()
I.language()
I.capital()

None
New Delhi
'''

# Eg:3
# polymporphisam objects
'''
class c1:
    def f1(slef):
        print("class 1")

class c2(c1):
    def f1(slef):
        print("class 2")

obj1 = c2()
obj1.f1()

class 2
'''
'''
class c1:
    def f1(slef):
        print("class 1")

class c2(c1):
    def f1(slef):
        super().f1()
        print("class 2")

obj1 = c2()
obj1.f1()

class 1
class 2
'''
# Eg:4
'''
class c1:
    def f1(slef):
        print("class 1")

class c2(c1):
    def f1(slef):
        print("class 2")

obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()

display(obj1)
display(obj2)

class 2
class 1
'''

# changing the functionally of built in function
'''
class shooping:
    def __init__(self, l1):
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length

s = shooping([1,2,3,4,5])
print(len(s))
#print(len(s))

5
'''

'''
a = 9
b = 6
#print(a+b)
#print(a.__add__(b)) # number method

# int()
#print(a.__sub__(b))
len()
'''

# ! Method overloading
#Eg:1
'''
class suming:
    def add(self,a,b):
        print(a+b)

    def add(self,a,b,c):
        print(a+b+c)

s = suming()
s.add(4,5,1)

10
'''

# Eg:2
'''
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)

obj= summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)

2
7
6
'''

# ! ----------> Abstraction

