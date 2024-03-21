'''
eg:3
take the values lenth and breadth of a from user and cheack if it is square or not
'''
'''
length=int(input("enter value:"))
breadth=int(input("enter value:"))
if length==breadth:
    print("it is a square")
else:
    print("it is not a square")


enter value:5
enter value:5
it is a square

'''
'''
eg:4
python program to cheack whether the given interger is mul of bpth 5 and 7
'''
'''
n= int(input("enter the number: "))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")

enter the number: 35
yes
'''
'''
eg ; 4
write a program to accept the cost price of a bike and display the road tax to the be paid  according to the following criteria

cost price (in rs)                               tax
>100000                                          15% + discount 6%
>50000 and <= 100000                             10%
<= 50000                                         5%
'''
'''
price= int(input("enter the price: "))
amount= 0
if price>=100000:
    discount= 100000*(6/100)
    value=price-discount
    amount=value*(15/100)
    print(value+amount)
   
enter the price: 120000
131100.0
'''
'''
write a program to accept the cost price of a bike and display the road tax to the be paid  according to the following criteria

cost price (in rs)                               tax
>100000                                          15% + discount 6%
<100000                                           5%
'''
'''
price=int(input("enter the value: "))
total=0
if price>=100000:
          discount = price*(6/100)
          value = price  + discount
          tax=value*(15/100)
          total=value+tax
else:
    tax=price*(5/100)
    total=price+tax
print("the onroad cost of bike is: ",total)

enter the value: 200000
the onroad cost of bike is:  243800.0
'''
'''
# if elif
#eg:1
a=7
b=9
c=3

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("C is greater")

B is greater
'''
#Eg:2
# A school has having following rules for grading system
#a. below 25 - F
#b. 25 to 45 - E
#C. 45 to 50 - D
#d. 50 to 60 - c
#e. 60 to 80 - B
#f. Above 80 - A
# Ask uer to enter marks and print the corosponding grade
'''
mark = int(input("enter mark: "))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>=40 and mark<50:
    print("D")
else:
    print("Fail")


enter mark: 94
A

'''

#short hand else
#eg:1
'''
a=9
b=6
if a>b:
    print("A")
else:
    print("B")

A

'''
# rules
# 1.statement inside the if condition have to be present at first
# 2.elif cannot be used in short hand if else
# 3.always it have to end with else.
'''
a=9
b=6
print("A") if a>b else print("B")

A
'''

# code to check the given cahr is vowel or consonment
'''
char = input("enter the char:")
if char=="a" or char =='e' or char =='i'or char =='o' or char =='u':
    print("is a vowel")
else:
    print("its consonent")

enter the char:a
is a vowel
'''
#or
'''
char = input("enter the char:")
str1="aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonent")

enter the char:eenter the char:a
is a vowel
'''
# ! ----> elif ladder using short hand if else
'''
a=8
b=5
c=6

print("A is greater") if a>b and b>c else print("B is greater") if b>a and b>c else print("c is greater")

c is greater
'''

# -----> looping

# looping can be implemented
# for loop
# while loop

#----> for loop
# for loop is used fpr iteration, if we know the number of times the loop have to run
# it is used to literate the iterables like as (string, list, tuple,...etc)

# todo --> syntax for loop

#for syntax in c
#for(i=0;i<10;i++){
#     print("hello");
# }

# for syntax in python
# for userdefined_variable in range (start, end, step): default step value is 1
#     statement
#     statement
#     statement

# Eg:1
#to print the value from 1 to 10 using for loop
'''
for i in range (0,10):  #(n, n-1)
    print("i")

0
1
2
3
4
5
6
7
8
9

'''

# Eg:2
'''
for val in range(1,15,2):
    print(val)

1
3
5
7
9
11
13
'''
'''
for val in range(1,15,3):
    print(val)
    
1
4
7
10
13
'''
# Eg:3
'''
for val in range(10,0,-1):
    print(val)

10
9
8
7
6
5
4
3
2
1
'''

# Eg:4
'''
for val in range(10,0,1):
    print(val)

#no output
'''
# Eg:5
#print the output of 7 th muitipication table from 21 to 43
'''
for val in range(1,10+1):
    print(val*7)

7
14
21
28
35
42
49
56
63
70
'''
# Eg:6---> method 1
'''
for val in range(1,10+1):
    print('7','x',val,'=',val*7)

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
'''

# Eg:6---> method 2
'''
for val in range(1,10+1):
    ans="7 x {}= {}"
    print(ans.format(val,val*7))
    
7 x 1= 7
7 x 2= 14
7 x 3= 21
7 x 4= 28
7 x 5= 35
7 x 6= 42
7 x 7= 49
7 x 8= 56
7 x 9= 63
7 x 10= 70
'''

# Eg:6---> method 3
'''
for val in range(1,10+1):
    print(f"7 x {val}={val*7}")

7 x 1=7
7 x 2=14
7 x 3=21
7 x 4=28
7 x 5=35
7 x 6=42
7 x 7=49
7 x 8=56
7 x 9=63
7 x 10=70
'''
# Eg:7
#breack ---> used to terminate the loop
'''
for val in range (1,10):
    if val ==6:
        break
    print(val)

1
2
3
4
5
'''
'''
for val in range (1,10):
    if val ==6:
        print(val)
        break

6
'''

# ! Continue --->
#Eg:1
'''
for val in range (1,10):
    if val ==6:
        continue
    print(val)

1
2
3
4
5
7
8
9
'''
# practice problems
# print the even number b/w 20 to 40
'''
for val in range(20,40,2):
    print(val)

20
22
24
26
28
30
32
34
36
38
'''
# ! ------> while loop
#while is used when we do not kbnoe the number of times the loop have to run
#to iterate the non iterable elements while loop is used

# to do syntax
# initialisation
# while condition
#     statement
#     incre or decre

#Eg:1

#to iterate number from 1 to 10
'''
i=0
while i<11:
    print(i)
    i=i+1 # or +=1

0
1
2
3
4
5
6
7
8
9
10
'''

#Eg:2
#10,1

'''
i=10
while i>0:
    print(i)
    i-=1

10
9
8
7
6
5
4
3
2
1
'''

# ! -----> 1-4+9-16+25=15
'''
n=int(input("enter number: "))
sum=0
for val in range(1, n+1):
    sq=val*val
    if val %2==0:
        sum=sum+val
    else:
        sum=sum-sq
print(sum)

enter number: 5
-29
'''
# for loop practice
# write a program to display sum of odd numbers and even
# numbers that fall between
# 12 abd 37c(including both numbers)

# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432

