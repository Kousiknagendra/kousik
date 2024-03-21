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
# The process of hiding implementation details is abstraction

# Eg:1
'''
from abc import ABC, abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")

class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")

    def name(self):
        print("I am triangle")

    def sides(self):
        pass

class square(shapes):
    def sqaure(self):
        print("4 sides")

tr = triangle()
tr.triangle_sides()
tr.name()

3 sides
I am triangle
'''

# ! ------------->Rules to define absrarct class1

# 1.) Abstract class cannot be instantained
# 2.) from abc import ABC, absract method
# 3.) sub class the normal class with ABC
# 4.) convert the normal method inside the abstract class to abstact method
# 5.) all the child classes have to be sub classed with abstract class 
# 6.) the abstract method should be present in the child classes

# Eg:2
# super()  ------> used to access the present class method from child class method
'''
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass

class2 = c2()
class2.m2()
    
This is abstract class
Iam child 1
'''
# Eg:3
'''
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "sidd1994$"
        return pswd

class login(password):
    def validate(self,name,passwrd):
        if super().pwd() == passwrd:
            print("welcome", name, "!!")
            print(" Login succesfull")
        else:
            print("Please check the password")

    def pwd(self):
        pass


login = login()
name = input("Enter the name: ")
pwd = input("Enter the password: ")
login.validate(name, pwd)

Enter the name: kousik
Enter the password: 123456
Please check the password
123456
123456
'''

# ! Encapsulation
#Eg:1

'''
class car:
    name = "BMW"

c1 = car()
print(c1.name)
c1.name = "Audi"
print(c1.name)

BMW
Audi
'''

# Eg:2

'''
class c1:
    __phone = '9876543210'

    def display(self):
        print(self.__phone)
c = c1()
c.display()

9876543210

'''

# ------> Eg:3
# declare private method
'''
class class1:
    def __m1(self):
        print("Iam private method")

    def __init__(self):
        self.__m1()

c = class1()
#c.__m1() #error

Iam private method
'''

# nested class
'''
class class1:
    class class2:
        name = "Kousik"

        def display(self):
            print(self.name)
    obj1 = class2()

obj = class1()
obj.obj1.display()

Kousik
'''
