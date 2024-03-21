# -----> while loop
# -----> breack using while loop

# eg:1
#iterate from 20 to 30 and breaxck the loop in 27
'''
i=20
while i<31:
    if i == 27:
        break
    print(i)
    i+=1

20
21
22
23
24
25
26    
'''
#2)
'''
i=20
while i<31:
    print(i)
    if i ==27:
        break
    i+=1

20
21
22
23
24
25
26
27
'''

#3
'''
i = 20
while i<31:
    if i ==27:
        print(i)
        break
    i+=1

27
'''

#! ----> continue
#eg:1
'''
i=20
while i in range (20,30):
    i = i+1
    if i == 27:
        continue
    print(i)
  
21
22
23
24
25
26
28
29
30
'''

#eg:
#write to iterate from 12 to 22
#find all sum of numbeers
'''
i =12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)
    
187
'''

#eg
'''
i=12
add=0
while i<=23:
    add+=i
    i+=1
    if i==23:
        print("sum of number is:",add)

sum of number is: 187
'''

#eg : find the avg valuue 20 to 25
'''
i =20
sum=0
while i<=25:
    sum=sum+i
    i+=1
print(sum/6)

22.5
'''

#eg: find the avg valuue 20 to 30
'''
i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)

25.0
'''

#----------> Nested for loop
#eg:1
'''
for i in range(1,3+1):
    for j in range(1,4+1):
        print(i,j)

1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
'''

#eg; type squre format of *

#* * * * 
#* * * * 
#* * * * 
#* * * *

'''
for i in range(4):
    for j in range(4):
        print("*")

*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
'''
#eg;
'''
for i in range(4):
    for j in range(4):
        print("*", end=" ")

* * * * * * * * * * * * * * * * 
'''

#eg;
'''
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

* * * * 
* * * * 
* * * * 
* * * * 
'''
#eg;
'''
for row in range(5):
    for col in range(5):
        print(row, end=" ")
    print()


0 0 0 0 0 
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
'''
#eg;
'''
sum=0
for row in range(5):
    for col in range(5):
        sum=sum+1
        print(sum, end=" ")
    print()

1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25 
'''

# to print stars right angled triangle
'''
for i in range(0,6):
    for j in range(0, i):
        print("*", end=" ")
    print()

* 
* * 
* * * 
* * * * 
* * * * *

'''

# to print stars right angled triangle inverted
'''
for i in range(0,6):
    for j in range(i,6):
        print("*", end=" ")
    print()

* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

'''

# to print stars in suare shape

# * * * * *
# *       *
# *       *
# *       *
# * * * * *
'''
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row==0 or row ==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

* * * * * 
*       * 
*       * 
*       * 
* * * * * 

'''

#      *
#    * * *
#   * * * *
#  * * * * *

'''
for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


      *     
    * * *   
  * * * * * 
            
'''



# *
# * *
# *   *
# *     *
# *       *
# * * * * * *
'''
for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

*           
* *         
*   *       
*     *     
*       *   
* * * * * * 
'''


#----> List

#---> Datatypes
# Primary

# Number---> int,float,complex
# string
# Boolean
# none

# Collection
# List
# tuple
# set
# dictionary

#---> List

#1.) If the collection of elements are surrounded by square brackets, it is considered to be list
##Eg:1
   #l1 = [4, 7, 9, 89, "hello", 7+9], [8,9,0]

#characteristics of list
#1.)list have to surrounded by[]
#2.)It is mutable ( the elements in the list are changable)
#3.)Every element inside list in indexed
#4.)The elements inside list will be ordered format
#5.)It can hold duplicate values
#6.)it is heterogenous

# TO access the elements in list
#lst1=[1,4,1,7,89.7,5,"p","i",5,2,20]
#print(l1)

#--->Indexing
#The collection datatypes like list, tuple, string, the elements will be alloted with predefined unique value called index value

#We have 2 types of indexing
#positive indexing --> starts with 0 from left hand side
#Negative indexing --> starts with -1 from right hand side

#--->Positive indexing
'''print(lst1[0])
print(lst1[4])
print(lst1[10])
print(lst1[20]) #--->error'''

#---> Negative indexing
#lst1=[1,4,1,7,89.7,5,"p","i",]
#print(lst1[-1])
#print(lst1[-4])

# -----> slicing

'''
lst1 = [1,4,1,7,89.7,7.5,"p","i"]
# lst1[start_index:end_index:step]
print(lst1[0:4])
print(lst1[6:8])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])
print(lst1[0:7:1])
print(lst1[0:7:2])

[1, 4, 1, 7]
['p', 'i']
[1, 4, 1, 7, 89.7]
[7, 89.7, 7.5, 'p', 'i']
[1, 4, 1, 7, 89.7, 7.5, 'p', 'i']
[1, 4, 1, 7, 89.7, 7.5, 'p']
[1, 1, 89.7, 'p']
'''
'''
lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(lst1[-4:-1])
print(lst1[-1:-4])

[89.7, 7.5, 'p']
[]

'''
'''
lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(lst1[-7:-1])
print(lst1[-7:-1:2])

[4, 1, 7, 89.7, 7.5, 'p']
[4, 7, 7.5]
'''

#! To insert ot add element inside list
# append()-> used to add elelement at last position of list
'''
l1=[9, 8, 0, 6]
l1.append("car")
print(l1)

[9, 8, 0, 6, 'car']
'''










#s1="hello world to all"
