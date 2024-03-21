# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]


# 1st
'''
s1="hello world"
fst = s1[0].upper()
lst =s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)

Hello worlD
'''

# 2nd
'''
n = 128
temp = n
f1 = 0
while n!= 0:
    rem = n%10
    check = temp%rem
    if check!=0:
        f1=1
    n=n// 10   
if f1==0:
    print("YES")
else:
    print("N0")
'''
'''
n=128
if n % 1==0 and n % 2==0 and n % 8==0:
    print("Yes")
else:
    print("No")
'''

# 3rd
'''
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[]
for val in range(len(l1)):
    ans=l1[val]+l2[val]
    l3.append(ans)
print(l3)

[6, 8, 10, 12]
'''

# ! -----> set
# characteristics of set
#1.) set can be created using{}
#2.) The element inside set are not indexed
#3.) Does not allow duplicate values
#4.) it unordered
#5.) heterogenous ------> accept only unmutable datatypes
#6.) mutable or changable


# Eg:1
'''
s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)

{89, (8, 7, 5), 'e', 7.76, 9, (8+7j), 'truck'}
'''

#eg:2
'''
s2={5,8,9,[9,0]}
print(s2) #-----------> error
'''

#eg:3
#min(),max(),len()

#eg
# to add element inside list
'''
s1={8,78,67,'u'}
#add()
s1.add(43)
print(s1)

{67, 8, 43, 'u', 78}
'''

#update
'''
s1={8,78,67,'u'}
s1.update([9,0])
print(s1)

{0, 67, 8, 9, 78, 'u'}
'''

# to delete element iside list
'''
s1={8,78,67,'u'}

# pop()
s1.pop()
print(s1)

{67, 'u', 78}
'''

#remove
'''
s1.remove(78)
print(s1)

{8, 67, 'u'}
'''

#discard
'''
s1={8,78,67,'u'}
s1.discard(67)
print(s1)

{8, 'u', 78}
'''

# clear()
#l1 = {}
#print(type(l1)) #---> datatype is dict

#s1 = set() # to create empty set
#print(type(s1))


'''
s1 = {8,9,0}
s1.clear()
print(s1)
'''

'''
s1 = {8,9,0}
del s1
print(s1)
'''
# del s1
# print(s1)


# * join the sets
'''
s1 = {9,0,8}
s1 = {9.90,"card",'t',56}
#union()
s3 = s1.union(s2)
print(s3)
'''
# * intersection() --> to get common elements inside set
'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.intersection(s2))

{5, 6}
'''
# * difference()
'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))

{4}
{8, 7}
{4, 7, 8}
'''

# isdsjoit(), issubset(), issuperset()
'''

s1 = {8,9,0}
s2 = {6,7,5,8,9,0}
print(s1.issubset(s2))
print(s2.issuperset(s1))

True
True
'''
'''
s1= {1,2,3,4,5}
s2= {3,2,7,8,9}

for val in s1:
    if val in s2:
        str1= " Its joint set"
print(str1)

Its joint set
'''

# ! --------> dictionary

# ? Char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key, value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed, duplicate value are allowed
# 5.) It is unindexed
# 6.) It is ordered
# 7.) key does not allow mutable data types,values allow mutable datatype 

# * to access element in dictionary

#print(d1)
#or
#to access the values, have to use key
#print(1[1]) # ---> 100

# ? some common functions
#len(),min(),max()
#print(min(d1))
#print(max(d1))


# ? dictionary  based function
# to add element(key and value pair) in dict
'''
d1 = {1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)

{1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
'''

# to replace a value in dictonary
'''
d1={1:100,2:200,3:300,4:400}
d1[2]="mango"
print(d1)

{1: 100, 2: 'mango', 3: 300, 4: 400}
'''

# delete elememt from dictionary
'''
d1={1:100,2:200,3:300,4:400}
#pop.item()
d1.popitem()
print(d1)

{1: 100, 2: 200, 3: 300}
'''

#pop()
'''
d1={1:100,2:200,3:300,4:400}
d1.pop(2)
print(d1)

{1: 100, 3: 300, 4: 400}
'''

# clear(), del

#join to dictionary
#update()
'''
d1={1:100, 2:200, 3:300, 4:400}
d2={"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)

{1: 100, 2: 200, 3: 300, 4: 400, 'a': 'apple', 'b': 'boy', 'g': 'game'}

'''

#get()
'''
d1={1:100, 2:200, 3:300, 4:400}
print(d1[90])
print(d1.get(90))
'''
# to print the all keys
'''
d1={1:100, 2:200, 3:300, 4:400}
print(d1.keys())
print(type(d1.keys))

dict_keys([1, 2, 3, 4])
<class 'builtin_function_or_method'>
'''
'''
d1={1:100, 2:200, 3:300, 4:400}
print(d1.values())

dict_values([100, 200, 300, 400])
'''

# Iterating dictonary
'''
d1={1:100, 2:200, 3:300, 4:400}
for val in d1: # To iterate keys alone
    print(val)

1
2
3
4
'''
'''
d1={1:100, 2:200, 3:300, 4:400}
for val in d1.values():  # To iterate values alone
    print(val)

100
200
300
400
'''



#!------> problem 3
'''
l1=[1,2,3,4] # key
l2=["a", "b", "c", "d"] # value

#{1:'a'}
d1 = {}
for val in range(len(l1)):
    d1[l1[val]]=l2[val]
print(d1)
    
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

'''
# to get both key and values
'''
d1={1:100, 2:200, 3:300, 4:400}
for key, val in d1.items():
    print(key, val)


1 100
2 200
3 300
4 400
'''

#eg:1
'''
d1= {1:100,'a':200, 4.5:"hello"}
print(d1)
print(len(d1))

{1: 100, 'a': 200, 4.5: 'hello'}
3
'''


# problem 1

#1.) swap elemwnts in string list
# The original list is :["Gfg", "best", "for", "Geeks"]
# List after performing character swaps:]"efg", "is", "bGst", "for", "eGGks"]
'''
n=int(input("Enter the num of times: "))
integer=[]
float_value=[]
string=[]

for val in range(n):
    value=eval(input("Enter the values:"))
    if type(value)==int:
        integer.append(value)
    elif type(value)==float:
        float_value.append(value)
    elif type(value)==str:
        string.append(value)
    else:
        print("pls provide data in int,float,string")

print(integer)
print(float_value)
print(string)

Enter the num of times: 10
Enter the values:1
Enter the values:2
Enter the values:3
Enter the values:4.5
Enter the values:6.7
Enter the values:8.9
Enter the values:'hello'
Enter the values:9
Enter the values:'world'
Enter the values:'kousik'
[1, 2, 3, 9]
[4.5, 6.7, 8.9]
['hello', 'world', 'kousik']
'''

# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}

''''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

l1=set1 ^ set2
print(l1)

{20, 70, 10, 60}
'''
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set()
for val in set1:
    if val not in set2:
         set3.add(val)
for val in set2:
    if val not in set1:
        if val not in set1:
            set3.add(val)
print(set3)

{10, 20, 70, 60}
'''

# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']

