'''
a, b = 78
print(a, b)
'''
'''
a=7, 8
print(a)
print(type(a))
'''
'''
a=b, c=4, 2
print(a,b,c)
'''
'''
-----> changing variables
eg:1
a=7
b=5
temp=a
a=b
b=temp
print(a, b)
'''
'''
eg:2
a=7
b=5
a=a+b
b=a-b
a=a-b
print(a, b)
'''
'''
eg:3
a=7
b=5
a, b=b, a
print(a,b)
'''
'''
eg:4
a=7
b=5
a=a*b
b=a/b
a=a/b
print(int(a),int(b))
'''
'''
--->used to find the memory adress of the variable
a=7
b=8
print(id(a))
print(id(b))
'''
'''
-->Keywords
keywords are preserved words which provides special meaning to compiler or interchanger

import keyword
print(keyword.kwlist)

'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
'''
'''
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
<class 'list'>
'''
'''
import keyword
print(keyword.is keyword("kousik"))

False
'''
'''
#--->Literals
Literal is the constant value assigned to a variable
A variable is considers to be constant when it is defines
in caps

a=78 # a nis variable
A=78 # A uis constant
'''
'''
l1 = [9,8,0]
l1 = [6, 7, 8, 0]
l1 = 89
'''
'''
hash()---> it creates a hask value for constant datatypes anfd provides error for non constant sata types

n1=89+7j
print(hash(n1))

7000110

f1=[7,8,9]
print(hash(f1)) #error ---> list is non-constantor multiple datatype

7000110
6950854851967187257

a=9
b=9
b=90
print(id(a))
print(id(b))

140721710189240
140721710191832

#!--->Operators
?operators are symbols which is used to perform various oprations b/w 2 or more operands 

Arthematic
Assignement
Logical
relational or comparision
bitwise
identity
membership

# *---> Arthematic ---> +,-,*,/,%,//,**

eg:1
a=8
b=6
c=9
print(a+b+c)

23

#input() --> used to get the routine input
n1=input("Enter the value:")
print(n1)

https://medium.com/@a.tavallaie/python-programming-libraries-for-mechanical-engineer-409cf994efdd
