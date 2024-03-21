# --------> common function  for list
'''
l1=[6,7,8,9,0]

print(len(l1))
print(max(l1))
print(min(l1))

5
9
0
'''

#l1=[6,7,8,9,"p","i"]
#print(max(l1)) -----------> error caz its comnbination of int and string
#pirnt(min(l1)) -----------> error caz its comnbination of int and string
'''
l1=[6,7,8,9,0,8.9,-5,0.78]
print(min(l1))

-5
'''
'''
l1=[6,7,8,9,0,8.89,-5,0.78]
# index() --> to get index value of specific element
print(l1.index(9))

3
'''
'''
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
# count() --> how many no.of times an element is repeted
print(l1.count(6))

3
'''
#! some functions which is specifically used list
'''
# to add elememt inside list
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
# insert (index_value, element) --> to add specific index position
l1.insert(2, "cars")
print(l1)

[6, 6, 'cars', 6, 7, 8, 9, 0, 8.89, -5, 0.78]
'''

# to delete element from list
'''
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
# pop() ---> last element will be deleted
l1.pop()
print(l1)

[6, 6, 6, 7, 8, 9, 0, 8.89, -5]
'''
# pop(index_value) ---> used to delete element at specific index
'''
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
l1.pop(4) #
print(l1)

[6, 6, 6, 7, 9, 0, 8.89, -5, 0.78]
'''

# remove(element) --> used to delete element directly
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.remove(6.76)
print(l1)

[2, 3, 2, 3, 4, 32, 98.5, -94]
'''
# clear() --> to complete delete all element in list
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.clear()
print(l1)

()
'''

#del ---> to delete the list
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
del(l1)
print(l1)
'''
# ----> jion 2 lists
'''
l1=[9,0,8]
l2=["p","o","t",34]
print(l1+l2)

[9, 0, 8, 'p', 'o', 't', 34]
'''
# extend() ---> to combine 2 lists
'''
l1=[9,0,8]
l2=["p","o","t",34]
l1.extend(l2)
print(l1)

[9, 0, 8, 'p', 'o', 't', 34]
'''

# ? ---> copy()

'''
l1 = [6, 7, 8,9, 3]
l2 = l1.copy()
print(l2)
print(l1)
print(id(l1))
print(id(l2))

[6, 7, 8, 9, 3]
[6, 7, 8, 9, 3]
1410146694208
1410103044992
'''

# diff b/w shallow copy and deep copy
#shallow copy
'''
import copy
l1 = [8,9,0,[5,6],[3,2,1]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)

[8, 9, 0, [5, 6], [3, 2, 1], 890]
[8, 9, 0, [5, 6], [3, 2, 1]]
'''

#deep copy
'''
import copy
l1=[8,9,0,[5,6],[3,2,1]]
print(l1[-1][1]) #---> to index nested list

l2=copy.deepcopy(l1)
l1.append(209)
print(l1)
print(l2)

2
[8, 9, 0, [5, 6], [3, 2, 1], 209]
[8, 9, 0, [5, 6], [3, 2, 1]]
'''

# sort --> arrange elements in list in ascending or desending order
'''
l1=[9,7,45,0,-6,5,12]
l1.sort() #to arrange in asceding order
print(l1)

[-6, 0, 5, 7, 9, 12, 45]
'''
'''
l1=[9,7,45,0,-6,5,12]
l1.sort(reverse=True) # to arrange in desendintg order 
print(l1)

[45, 12, 9, 7, 5, 0, -6]

'''

# ? list constructor
# * list() --> to cover other collection datatype to list
'''
l3 = ((8, 9,0))
print(list(l3))

[8, 9, 0]

'''
'''
l4 = (8,9)
print(list(l4))

[8, 9]

'''

# ! ---> nested list
'''
l1 = [8,9,[0,8,7],["p","o","y"],[8, 't']]
print(l1[-2][1])

o

'''
'''
l1 = [8,9,[0,8,7],["p","o","y"],[8, 't']]
print(l1[1:4])
print(l1[1:-1])
[9, [0, 8, 7], ['p', 'o', 'y']]
[9, [0, 8, 7], ['p', 'o', 'y']]

'''

# to delete "t" from l1
'''
l1 = [8,9,[0,8,7],["p","o","y"],[8,'t']]
l1[-1].remove('t')
print(l1)

[8, 9, [0, 8, 7], ['p', 'o', 'y'], [8]]
'''

# combine these ["p","o",'y'],[8,'t']
'''
l1=["p","o",'y']
l2=[8,'t']
l1.extend(l2)
print(l1)

['p', 'o', 'y', 8, 't']
'''

# -------> Tupule
# char of tuple

#1.) tuple have to be surrounded by ()
#2.) The element inside tuple are not changable
#3.) The element inside tuple are indexed
#4.) The element will excuted in order
#5.) It is heterogenous
#6.) It allow duplicate element

#eg:
'''
t1=(8,8,9,6,5,5.78,[9,0],(6,8),"hey", 9+6j)
print(t1)
print(type(t1))

(8, 8, 9, 6, 5, 5.78, [9, 0], (6, 8), 'hey', (9+6j))
<class 'tuple'>
'''
# indexing,slicing are all same as list
'''
l1=(8)
print(type(l1))

<class 'int'>
'''
'''
t1=8,9
print(type(t1))

<class 'tuple'>
'''
'''
t2=8,
print(type(t2))

<class 'tuple'>
'''

#len(), min(),max(),index(),count() ---> all same as list

# to add  element inside tuple ---> cannot add
# cannot delete any element from tuple


# * jon 2 tuples
'''
t1 = (8, 9, 0)
t2 = (6, 7, 8)
print(t1 + t2)

(8, 9, 0, 6, 7, 8)
'''
# To add all element inside list and tuple
#sum()
'''
l1 = (8, 9, 7, 6)
print(sum(l1))

30
'''

# * sort tuple
'''
t1 = (8, 9,0, 89, 12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1, reverse=True)))

(0, 8, 9, 12, 89)
(89, 12, 9, 8, 0)

'''
# * Iterate list and tuples
'''
l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)

9
8
0
6
5
'''

# Iterate based on index value
'''
l1=[9,8,0,6,5,7,36,54,55,6,43,5,66]
for i in range(0,len(l1)):
    print(l1[i])

9
8
0
6
5
7
36
54
55
6
43
5
66
'''


# ! ---> strings
'''
s1='o'
print(type(s1))

<class 'str'>
'''
'''
s1='u'
print(type(s1))

<class 'str'>
'''
'''
s1= "hello world"
# to acces string
print(s1)

hello world
'''
'''
s1= "hello world"
print(s1[0:5])

hello
'''

#len(), min(),max(),index(),count()
'''
s1="hello world"
print(len(s1))
print(max(s1))
print(min(s1))


11
w
'''
'''
s1="hello world"
#ord ----> used to find the ASCII value of a charecter
s1='u'
print(ord('u'))

117
'''

# functions of string
'''
s1="hello world"
# to convert all charecteres tyo upper case
print(s1.upper())

HELLO WORLD
'''
'''
s1="HELLO WORLD"
# to convert all cases in lower case
print(s1.lower())

hello world
'''

# strip()
'''
s1=" where are you?"
print(s1)

 where are you?
'''
# strip() ---> to eliminate the space in begining and end of string
'''
s1=" where are you?"
print(s1.lstrip())   ---> to eliminate the space in begining
print(s1.rstrip())   ---> to eliminate the space in ending
print(s1.strip())

where are you?
'''

# spilit() ---------> to split the words in string basesd on a charecter
'''
s1=" where are you?"
print(s1.split())
print(s1.split("r"))
print(s1.split("e"))

['where', 'are', 'you?']
[' whe', 'e a', 'e you?']
'''
# replace()---->
'''
s1=" where are you?"
print(s1.replace('r','&&'))

 whe&&e a&&e you?
'''
# swapcase()---> to convert captital to small and small to capital at a time
'''
s1="HEY there"
print(s1.swapcase())

hey THERE
'''

# title() --> to erite the string in format of title
'''
s1='never give up'
print(s1.title())

Never Give Up
'''
# jion the strings
'''
s1='hello'
s2='world'
print(s1+s2)

helloworld
'''

s1='''
how are you
i am fine
hey there
'''
#spilitlines() --> used to split the string based on lines
'''
print(s1.splitlines())

['', 'how are you', 'i am fine', 'hey there']
'''
# find() --->
'''
s1="hello world"
print(s1.find('h'))
print(s1.index('h'))

0
0
'''

# join() --->
'''
l1=["hey","there"]
print(" ".join(l1))
print("$".join(l1))

hey there
hey$there
'''

'''
s1="Welcome to all"
print(s1.endswith('l'))
print(s1.startswith('W'))

True
True
'''
'''
s1="67"
print(type(s1))
print(s1.isdigit())

<class 'str'>
True
'''
# print the string in reverse manner
'''
s1="Welcome to all"
print(s1[::1])
print(s1[::-1])

Welcome to all
lla ot emocleW
'''

#eg:1
'''
s1="HEY there you aRE"
for i in s1:
    print(i)

H
E
Y
 
t
h
e
r
e
 
y
o
u
 
a
R
E
'''
'''
s1="HEY there you aRE"
for i in s1:
    if i.islower():
        print(i)

t
h
e
r
e
y
o
u
a
'''
'''
s1="HEY there you aRE"
count=0
for i in s1:
    if i.islower():
        count+=1
print("the total num of lower case letters: ",count)

the total num of lower case letters:  9
'''

# eg:2
'''
s1='restarter'  # r ---> $
print(s1[0] + s1[1:].replace('r','$'))

resta$te$
'''

# eg:3
'''
s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop"
'''

'''
charecters=len(s1)
print(charecters)

498
'''
'''
words=s1.split(" ")
print(words)

['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry.', 'Lorem', 'Ipsum', 'has', 'been', 'the', "industry's", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s,', 'when', 'an', 'unknown', 'printer', 'took', 'a', 'galley', 'of', 'type', 'and', 'scrambled', 'it', 'to', 'make', 'a', 'type', 'specimen', 'book.', 'It', 'has', 'survived', 'not', 'only', 'five', 'centuries,', 'but', 'also', 'the', 'leap', 'into', 'electronic', 'typesetting,', 'remaining', 'essentially', 'unchanged.', 'It', 'was', 'popularised', 'in', 'the', '1960s', 'with', 'the', 'release', 'of', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages,', 'and', 'more', 'recently', 'with', 'desktop']
'''
'''
words=s1.split(" ")
print(len(words))

81
'''
'''
sentences=s1.split('.')
print(len(sentences))

4
'''
'''
sentences=s1.split('.')
for val in sentences:
    if val =='':
        index==sentences.index('')
        sentences.pop(index)
print(len(sentences))

4
'''
'''
space=0
for val in s1:
    if val ==" ":
        sapce=space+1
print(space)
'''

# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]


x=2,3,4,5
print(x)

a=2
b='3.77'
c=-8
str1='{0:4f}{0:3d}{2}{1}'.format(a,b,c)
print(str1)

print('printing numbers{0:x},{1:b}and{2:o}'.format(14,8,12))

a=[(2,4),(1,2),(3,9)]
a.sort()
print(a)

a={1,2,
