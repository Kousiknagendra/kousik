# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number


# ! Eg:3
'''
def profile(name,age,place):
    txt="my name is {}.Iam {}. years old.Iam from {}."
    print(txt.format(name,age,place))
profile("kousik",20,"Banglur")

my name is kousik.Iam 20. years old.Iam from Banglur.
'''

# Eg:4
# functions with return statement
# return
#1.) A variable declared inside function can be accessed outside the function using return
#2.) return does not print anything
#3.) we cannot write any code below return statement


'''
def f1():
    z = 8
f1()
print(z) # error---------> cannot use outside function
'''
'''
def f1(a,b):
    c = a*b
    return c
#print(f1(6, 8))
obj = f1(6, 8)
obj1 = f1(4, 6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

52
28
'''
# problem 1
# 123
'''
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("Not palindrome")
a = int(input("enter the value: "))
palindrome(a)

enter the value: 45
Not palindrome

enter the value: 121
121 palindrome
'''

# Based on the declaration of parameter and args
# Functions are divided into 5 categerioes

# positional args
# keyboard args
# default args
# variable lenth args
# keyboard variable length args

# positional args
# the position of parameter have to be same as position as arguments

#Eg:1
'''
def profile(name, phone, marks):
    txt = "My name is {}. My phone numm is {}. I got {} marks."
    print(txt.format(phone,name,marks))

profile(9876543210,"kousik",95)

My name is kousik. My phone numm is 9876543210. I got 95 marks.
'''

# ! Eg:1

#? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the
# funtions
'''
def profile(name,phone,mark):
    txt="My name is {}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))
profile(name="Kousik",mark=100,phone=96668686)

My name is Kousik. My phone number96668686. I got100 marks.
'''

# todo --------> Expectation of keyword args function
'''
def profile(name,phone,mark):
    txt="My name is {}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))
    
# profile(name="Kousik",1234567890,mark=100) #error -----> postional args follow keyword args
# profile(1234567890,name="Kousik",mark=98) #error -----> anme has multiple values
profile(name="Kousik",mark=100,phone=96668686)
'''

# default args
#eg:1
'''
def profile(name,phone,place="kadapa"):
    txt="My name is {}. My phone number{}. I am from {}."
    print(txt.format(name,phone,place))

profile("kousik",8767676767)


My name is kousik. My phone number8767676767. I am from kadapa.
'''
#eg:2

'''
def profile(name,phone,place="kadapa"):
    if place=="kadapa":
        txt="My name is {}. My phone number{}. I am from {}."
        print(txt.format(name,phone,place))
    else:
        print("You are not sign up")

profile("kousik",8767676767,"hyderabad")

You are not sign up
'''
'''
Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
'''
'''
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal
'''
# Expectation
'''
def profile(name,place="kadapa",phone): #error ---> coz default args
                                        # positional args
    if place=="kadapa":
        txt="My name is {}. My phone number{}. I am from {}."
        print(txt.format(name,phone,place))
    else:
        print("You are not sign up")

profile("kousik",8767676767)
'''

# ! variable length params
#eg:1
'''
def profile(*name):
    print("My name is", name)
profile("Kousik",'name2','name3')
'''
# to pass more than 1 arg to parameter means we use variable length args
# to convert normal parameter to variable length param, add * to the prefix of
#  parem
'''
name="Kousik","name1","name2"
def profile(*name):
    for val in name:
        print("My name is", val)
profile("Kousik",'name2','name3')


My name is Kousik
My name is name2
My name is name3
'''

# ! Eg:2
'''
def profile(*name,age):
    for val in name:
        print("My name is", val,"My age is", age)
profile("Kousik",'name2','name3',20)  ---> age has no args
'''
'''
def profile(age,*name):
    for val in name:
        print("My name is", val,"My age is", age)
profile(20,"Kousik",'name2','name3')


My name is Kousik My age is 20
My name is name2 My age is 20
My name is name3 My age is 20
'''

# keyboard variable length args
# kwrags ---> which is used to provide the args in the form of key value pair

# Eg:1
'''
def price(**price_list):
    print(price_list)

price(shirt=1000, ipone=80000)

{'shirt': 1000, 'ipone': 80000}
'''

#n=5
#{1:1,2:4,3;9,4:16,5:25}

'''
n=int(input("Enter the number:"))
d1 = {}
for val in range(1, n+1):
    d1[val]= val**2
print(d1)

Enter the number:5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
'''
def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val]= val**2
    print(d1)
dict1(5)

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

'''
d1={"a":100,"b":200,"c":300}
d1 = dict(a=100,b=200,c=300)
print(d1)

{'a': 100, 'b': 200, 'c': 300}
'''

# ! ---------> object oriented programming
# The panadigms of objects oriented progarmming are


# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! Class is a blue print of an object

#l1=[1,2,3,4,5,6]


# Eg:1
'''
class c1:
    name1 = "Kousik"
    print(name1)

Kousik
'''
# Eg:2
'''
class person:
    name = "Kousik"

c = person()
print(c.name)

Kousik
'''

# c = person() # c as object
# The process of creation of an object is called as Instantiation
# print(c.name)


#Eg:3
# create a method
# when function is creating with a class is called as method

'''
class person:
    def display(person): # it is a method
        print("Hello welcome to classes")

p = person()
p.display()

Hello welcome to classes
'''

# eg:4
# method with parameter
'''
class person:
    def display(person,name,age):
        print(name,age)

p = person()
p.display("Kousik",20)

Kousik 20
'''

# Eg:5
'''
class person1:
    fname = "Kousik" # attribute or static variable
    lname = "Nagendra"
    
    def first_name(self):
        print(self.fname)

    def full_name(self):
        print(self.fname+" "+self.lname)
        

p = person1()
p.first_name()
p.full_name()

Kousik
Kousik Nagendra
'''

# Eg:6
# constructors --> __init__()
# This is special method which has the ability to excute it self without
# calling it manuvally through the process of instantiaton

'''
class profile:
    def__init__(self): # constructor method
        print("hey")

p = profile() # exeution of constructor through this process
'''


