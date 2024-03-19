'''
wecp platform...
fotis academy.....website for puzzles..
#######################################################################################
# Exception handling in pyhton....
try:
	s=10/0
	print(s)
except ZeroDivisionError:
	print("can't divisible with zero...")
x='my name is sumanth and my full name is chinna sumanth kumar shetty'
try:
	print(x.index('sumanth kumar shetty'))
except Exception:
	print("string is not present in above main string...")
finally:
	print("Good Byee....")
print("Always Welcome....")
'''

######################################################################################
'''
# indexing to a string...
c='santhosh'
for i in c:
	print("The index of {} is :".format(i),c.index(i))
	'''
######################################################################################
'''
# indexing to a string...
s=input("Enter main string :")
d=input("enter an character :")
for i in s:
	if (i==d):
		print("Index of {} is :".format(i),s.index(i))
'''
######################################################################################
'''
# counting of characters in a string...
z='santhosh'
print(z.count('h'))

######################################################################################

# replace the old string with new string...
e=z.replace("santhosh","sumanth")
print(e)
'''
######################################################################################
'''
# sort function...
s=[3,2,1]
print(s)
print(id(s))
s.sort
print(s,id(s))
'''

######################################################################################
'''
# replace function and id of the objects checking....
d="sumanth"
print(d,id(d))
d=d.replace("sumanth","santhosh")
print(d,id(d))
'''
#####################################################################################
'''
# use of split function in python...
x="chinna sumanth kumar shetty"
k=x.split(" ")
print(k)
for i in k:
	print(i)
'''
#####################################################################################
'''
# taking maximum elements in a list...
d=list(map(int,input().rsplit(' ',2)))
print(d)

'''
####################################################################################
'''

a,b,c=map(int, input().rsplit(' ',2))
print(a)
print(b)
print(c)

'''
###################################################################################
'''
# backward split as rsplit().....
s="10,20,30,40,50,60,70,80"
l=s.rsplit(',',4)
for i in l:
	print(i)
	
# forward split()....
s="10,20,30,40,50,60,70,80"
l=s.split(',',4)
for i in l:
	print(i)
'''
##################################################################################
'''

# join() in python...
l=['chinna','sumanth','shetty']
print('-'.join(l))

'''
#################################################################################
'''
# string sequencing in python...
e="i am learning \"python\" programming language"
e='i am learning "python" programming language'
e=\'''i am learning "python" programming language\'''
print(e)

'''
##############################################################################
'''
# lower,upper,swapcase,title,capitalize,startswith,endswith,isalnum() in python...
s="i am learning PYTHON PROGRAMMING language"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
print(s.startswith('i'))
print(s.endswith('language'))
print(len(s))
print(s.isalnum())
print(s.isdigit())
print(s.isalpha())
print(s.islower())
print(s.isupper())
print(s.isspace())
print(s.istitle())


# output:
# sumanth@sumanth:~/Desktop$ python3 py.py 
# I AM LEARNING PYTHON PROGRAMMING LANGUAGE
# i am learning python programming language
# I AM LEARNING python programming LANGUAGE
# I Am Learning Python Programming Language
# I am learning python programming language
# True
# True
# 41
# False
# False
# False
# False
# False
# False
# False
'''
###############################################################################
'''
# sum,len,index,count,sort,reverse,pop,remove,clear,append,insert,extend,max,min
h=[10,20,30,40,50,90,80,60,70]
print(sum(h))
print(len(h))
print(h.index(30))
print(h.count(10))
h.sort()
print(h)
h.reverse()
print(h)
print(h.pop(0))
print(h)
h.remove(10)
print(h)
h.clear()
print(h)
h.append(10)
h.append(20)
print(h)
h.insert(1,30)
print(h)
ex=[50]
h.extend(ex)
print(h)
print(max(h))
print(min(h))

# output:
# sumanth@sumanth:~/Desktop$ python3 py.py
# 450
# 9
# 2
# 1
# [10, 20, 30, 40, 50, 60, 70, 80, 90]
# [90, 80, 70, 60, 50, 40, 30, 20, 10]
# 90
# [80, 70, 60, 50, 40, 30, 20, 10]
# [80, 70, 60, 50, 40, 30, 20]
# []
# [10, 20]
# [10, 30, 20]
# [10, 30, 20, 50]
# 50
#10
'''

###########################################################################################
'''
# string format function in python...
name='sumanth'
age=19
salary=100000
print("My name is {}.I am {} years old and i am earning {} rupees per month".format(name,age,salary))
'''
###########################################################################################
'''
# reverse an given string
t=input("ENTER A STRING: ")
print(t[::-1]) # by using slicing operator
for x in reversed(t): # by using reversed function
	print(x,end="")
print("\n")
print("".join(reversed(t))) # by using join method

# by using while loop...
u=input("enter a string: ")
i=len(u)-1
op=""
while i>=0:
	op=op+u[i]
	i=i-1
print(op)

'''
########################################################################################
'''
# reversing words of the string...
s="chinna sumanth kumar shetty"
g=s.split()
# using slicing operator...
e=(g[::-1])
print(" ".join(e))

# using for loop...
for i in e:
	print(i,end=" " )
'''
######################################################################################
'''
# Sorting the given alphanumeric string in python...
s="A4H90KG6"
a=""
n=""
for i in sorted(s):
	if(i.isalpha()):
		a=a+i
	else:
		n=n+i
print(a+n)
# output:
# sumanth@sumanth:~/Desktop$ python3 py.py
# AGHK0469 
'''
######################################################################################
'''
# difference between sort() and sorted() functions...
s=['sumanth','aeroplane','zebra','banana']
a=sorted(s)
print(a)
s.sort()
print(s)
'''
#####################################################################################
'''
# problem on string...
# input:    a4b3c2
# output:   aaaabbbcc
z=input("Enter the string : ")
u=p=0
for i in z:
	if i.isnumeric():
		u=z.index(i)
		p=(z[u-1]*int(i))
		print(p,end="")
print("\n")		

# output:
# sumanth@sumanth:~/Desktop$ python3 py.py
# aaaabbbcc
'''
#####################################################################################
'''
# slicing sub-tuple...
a='python'
b=[1,2,3]
a_tup=(a,b)
print(a_tup[1][1:])

# output:
# sumanth@sumanth:~/Desktop$ python3 py.py
#[2, 3] 
'''

#####################################################################################
'''
# spliting words from a given string...
d='chinna sumanth kumar shetty'
f=d.split(' ')
for i in f:
	print(i)
'''
#####################################################################################
'''
# print calendar...
import calendar
year=int(input())
print(calendar.calendar(year))
'''
####################################################################################
'''
# print particular month in an year...
from calendar import *
print(month(2023,6))
'''
####################################################################################
'''
# math module...
import math
print(math.fsum([1,2,3,4,5,6,7,8,9,10]))
print(math.sqrt(16))
print(math.pow(2,3))
# output:
# 55.0
# 4.0
# 8.0
'''
###################################################################################
'''
# reverse sort()
s=[1,2,34,5,66,4]
s.sort(reverse=True)
print(s)
'''
##################################################################################
# print natural numbers in a list
'''
s=[]
for i in range(10+1):
	s.append(i)
print(s)	

#####################################

print(list(range(10+1)))
'''
########################################
'''
# while loop
a=0
while a<10:
	print("assignment")
	a=a+1
	pass
'''
#######################################################################################
'''
# python patterns...
for i in range(5):
	for j in range(i+1):
		print("*",end=" ")
	print()
'''
#######################################################################################
'''
# linear search...
def linear_search(arr,length,target):
	for i in range(length):
		if(arr[i]==target):
			return i
	return -1

arr=list(map(int, input().split(",")))
length=len(arr)
target=int(input("Enter the target element: "))
result=linear_search(arr,length,target)
if(result==-1):
	print("element is not present in the array")
else:
	print("the element present at index: ",result)
'''
#########################################################################################
'''
# binary_search in python
def binary_search(arr,l,target):
	low=0
	high=l-1
	for i in range(l):
		mid=(low+high)//2
		if(target==arr[mid]):
			return mid
		elif(target>arr[mid]):
			low=mid+1
		elif(target<arr[mid]):
			high=mid-1
	return -1
			
arr=[12,34,56,78,99,100,283]
l=len(arr)
target=78
print(arr)
result=binary_search(arr,l,target)
if(result==-1): print("the element not found in an array")
else: print("the element present at index: ",result)
'''

#########################################################################################
'''
# lambda function in python...
x=10
y=10
sum=lambda x,y:x+y
result=sum(x,y)
print(result)


n=int(input("Enter the number: \n"))
a=lambda n:n*n
print(a(n))
'''
########################################################################################
'''
# Access nested list elements...
n_l=[2,3,56,7,8,[34,56]]
p=n_l[5][0]
print(p)
'''
########################################################################################
'''
# list using while loop...

w_l=[333,4,55,678,5,7,8,7,8,7]
i=0
while(i<len(w_l)):
	print(w_l[i])
	i=i+1
'''
###################################################################################################################
'''
# list using for loop...

f_l=[333,4,55,678,5,7,8,7,8,7]

#for i in range(len(f_l)):
#	print(f_l[i])
#for i in f_l:
#	print(i)
'''
###################################################################################################################
'''
# python functions and methods....
def a():  # function
	print("hello")
class S:  # method---------------what ever may be present functions in a class it is called methods.....
	def b(self):
		print("world")
a()
x=S()
x.b()
'''
###################################################################################################################
'''
# vowels in a string...
v=['a','i','e','o','u']
i=input()
f=[]
for t in range(len(i)):
	if i[t] in v:
		f.append(i[t])
print(f)		
'''
######################################################################################################################
'''
# tuple to list and list to tuple conversion....
a=(1,2,3,4,556,6,789,7)
print(type(a))
b=list(a)
print(type(b))
c=tuple(b)
print(type(c))
for i in c:
	print(i)
z=()
'''
#######################################################################################################################
'''
# printing random numbers using random module
#1st-way...
from random import *
e=randint(1000,9999)
print(e)
#2nd way...
import random
r=random.randint(1000,9999)
#3rd way....
import random as r
q=r.randint(1000,9999)
print(q)
'''
############################################################################################################################
'''
# manupulating the inbuilt print() function.... 
def out(n):
	print(n)
'''
#########################################################################################################################
'''
# for loop with variable length arguments....(*n) it is like a tuple...
def sum(*n):
	for i in n:print(i)
sum(1,2,3,4,5,6,7,8,9)
'''
########################################################################################################
'''
# NAME ERROR example....
a=10
print(b)
'''
#################################################################################################
'''
# Indentation Error example....
def f1():
print(0)
f1()
'''
###################################################################################################
'''
# Recursive functions-----> Factorial of a number....
def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)
	
print(fact(3))
'''
##############################################################################################
'''
# sum of natural numbers using recursive functions...
def sum(n):
	if n==1:
		return 1
	else:
		return n+sum(n-1)
print(sum(10))
'''
###############################################################################################
'''
# Fibonacci numbers using recursive function....not loops like (for),(while)....
def fibb(n):
	if n<=1:
		return n		
	else:
		return fibb(n-2)+fibb(n-1)
print(fibb(15))
'''
#########################################################################################
'''
# filter(function,sequence)
# Use of filter() function....
def is_even(x):
	if x%2==0:return True
	else:return False
l=[5,10,15,20,25,30,35,40,45,50]
s=list(filter(is_even,l))
print(s)

(OR)

l=[5,10,15,20,25,30,35,40,45,50]
s=list(filter(lambda x:x%2==0,l)
print(s)
'''
##################################################################################
'''
# List comprehensions in python....
l=[1,2,3,4,5,6,7,8,9,10]

#new_list = [expression for item in iterable if condition]

squares=[i**2 for i in l if i%2==0]
print(squares)
'''
######################################################################
'''
# Tuple comprehensions in python....
l=(1,2,3,4,5,6,7,8,9,10)

#new_tuple= (expression for item in iterable if condition)

square=(i**2 for i in l if i%2==0)
d=list(square)
print(d)
'''
##################################################################
'''
# map() function in python----->	map(function,sequence)

l=[1,2,3,4,5,6,7,8,9,10]
s=list(map(lambda x:2*x,l))
print(s)
'''
#################################################################################################################################################################
'''
# Generators in python     ----> in generators the objects or elements were not stored in memory. So that is the reason why it is responding...
import time
l1=(x*x for x in range(100))
for i in l1:print(i)
'''
################################################################################################################################################################
'''
# random module in python...
import random
my_list = [1, 2, 3, 4, 5]
random_sample = random.sample(my_list, 3)
print(random_sample)

l=['bob','hob','job','cob']
f=random.choice(l)
# uniform() generates random float point between given 2 numbers(a,b)
g=random.uniform(0,1)
# The random() in random module generates random float point between 0 and 1.0..
n=random.random()
print(f)
print(g)
print(n)
'''
##########################################################################################################
'''
# getting id of the variable which stored in computer storage
a=10
print(id(a))
'''
###########################################################################################################
'''
# ATM MACHINE PROBLEM
2
5 10
3 5 3 2 1
4 6
10 8 6 4

T,N,K,i	

11010
0010


t=int(input("no. of testcases: "))
for _ in range(t):
	n,k=list(map(int, input("elements for n and k : ").split()))
	i=list(map(int, input("elements for i: ").split()))
	r=""
	for v in i:
		if v<=k:
			r=r+"1"
			k=k-v
		else:
			r=r+"0"	
	print(r)
'''
####################################################################################################################
'''
# To get all variables in the python folder........
x=10
y=20
print(dir())
'''
####################################################################################################################
'''
# exception handling in python
try:
	print(2/2)	# Execute
	print(5/0)	# Not Execute
	print(1/1)	# Not Execute
except Exception:
	print(10/5)	# Execute
print(2/2)		# Execute

'''
##################################################################################################################
'''
# The PVM will shutdown....
import os
for i in range(10):
	if(i==8):
		os._exit(0)
	else:print(i)
print("I am using OS-Module")
'''
####################################################################################################################
'''
# program to shutdown the system...
import os
os.system("shutdown -h")
'''
#######################################################################################################################
'''
# else block will executed while there is no exception in the program....
try:
	print(2/2)
except Exception:
	print("Happy coding...")
else:
	print("Happy hacking")

'''
###################################################################################################################
'''
# Exception handling...
try:
	print(2/2)
	print(2/A)
except(ZeroDivisionError,ValueError,IndexError,NameError) as msg:
	print("The problem is: ",msg)
finally:
	print("This is the problem.....,")
'''
#####################################################################
'''
# functions in random library...
import random
a=[1,2,3,4,5,6,7,8,9]
print(random.sample(a,3))
'''
########################################################################################

'''
# Armstrong number
import math
a=input("Enter a number: ")
n=0
if(int(a)<10):
	print("Please enter number greater than 10...")
else:
	for i in a:
		n+=math.pow(int(i),len(a))
	if(int(n)==int(a)):
		print("ARMSTRONG NUMBER")
	else:print("NOT AN ARMSRONG NUMBER")
'''
################################################################################################
'''
# shutdown program....	
import os
u=list(input("Hi, User how can i help you...?\n").split())
arr=["power","off","shut","shutdown","close","turnoff"]
for i in u:
	if(i in arr):
		print("Are you sure,want to turnoff your system")
		inp=input("y/n\n")
		if(inp=="y" or "Y"):
			os.system("ls")	
		else:
			print("you may carry on...!")
else:
	print("HAPPY HACKING....!")
'''
#############################################################################################
'''
# Implementation of classes in python...
class Cal:
	def add(a,b):
		return(a+b)
	def sub(a,b):
		return(a-b)
	def mul(a,b):
		return(a*b)
	def div(a,b):
		return(a/b)
	def mod(a,b):
		return(a%b)
		
# Driver code...
print(Cal.add(1,2))	
'''
###################################################################
'''
# pattern
a=int(input("number of rows: "))
for i in range(a+1):
	print("*"*i)
for i in range(a+1):
	print((a-i)*"*")
'''
###########################################################
'''
# panindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        if(x<0):
            return False
        while(x>0): 			
            n=x%10  			
            rev=rev*10+n		
            x=x//10		
        return (n==x)
'''
###########################################################
'''
# find GCD (8,12)	
# METHOD-1
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

result = gcd(14,63)
print(result)
'''
###########################################################
'''
# gcd
# METHOD-2
def gcd(a,b):
	arr=[a,b]
	m=max(arr)
	for i in range(1,m+1):
		if(a % i == 0 and b % i == 0):
			gcd=i
	return gcd
print(gcd(100,25))
'''
############################################################
'''
4 divides both m,n and (12,8)
then m = ad, n = bd
    12 = 12*4, 8 = 8*4
so m-n = ad - bd = (a-b)d
   12-8 = 48 - 32 = (12-8)4
   	16        = 16
so gcd(12,8) = gcd(8,(12-8))
'''
############################################################
'''
# Euclid's algorithm for GCD:
def gcd(a,b):
	if a<b:
		a,b=b,a
	while (a%b)!=0:
		diff=a-b
		(a,b)=(max(b,diff),min(b,diff))
	return b
print(gcd(24,50))
'''	
###############################################################
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def display(self):
    	return self.items()

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.display())

print("Stack size:", stack.size())
print("Stack peek:", stack.peek())
'''
######################################################################
'''
# Digital sum
inp=38
output=38=3+8=11=1+1=2

def digital_root(number):
    while number >= 10:
        digit_sum = 0
        while number > 0:
            digit_sum += number % 10
            number //= 10
        number = digit_sum
    return number
print(digital_root(38))
'''
###############################################################
'''
import math
def isHappy(n):
        d = 0
        while n > 0:
            d = d + int(math.pow(n % 10,2))
            n //= 10
            n=d
        return n	
print(isHappy(19))
'''
################################################################
'''
# find single number in an array... 
arr=[4,1,2,1,2]
for i in arr:
	if arr.count(i) == 1:
		print(i) 
'''
###########################################################
'''
# BUBBLE SORT
# Input: nums = [2,2,3,1]
# Output: 1
n = [3,2,1]
for i in range(1,len(n)):
	for j in range(0,len(n)-1):
		if n[j]>n[i]:
			n[i],n[j]=n[j],n[i]
# [1,2,2,3]
s=set(n)
l=list(s)
print(l)
try:
	print(l[-3])
except:
	print(l[-1])
'''
##############################################################
'''
# third max number in an array...
class Solution:
    def thirdMax(nums):
        for i in range(1,len(nums)):
            for j in range(0,len(nums)-1):
                if nums[j] > nums[i]:
                    nums[i],nums[j] = nums[j],nums[i]
        s=set(nums)
        l=list(s)
        try:
        	return l[-3]
        except	:
        	return l[-1]

# driver code...
print(Solution.thirdMax([1,2]))
'''
####################################################################
'''
nums = [0,1,0,3,12]
arr = []
for i in nums:
	if i != 0:
		arr.insert(-2,i)
	else:
		arr.insert(-1,i)
print(arr)
'''
####################################################################
'''
# moving zeros to left corner...

class Solution:
    def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = []
        for i in nums:
            if i != 0:
                arr.insert(-2,i)
            else:
                arr.insert(-1,i)
        return arr
print(Solution.moveZeroes([0,1,0,3,12]))
'''
############################################################################
'''
n=15
arr = []
for i in range(1,n+1):
            if i % 5 == 0 and i % 3 == 0:
                arr.append("FizzBuzz")
            elif i % 3 == 0:
            	arr.append("Fizz")
            elif i % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(i))
print(arr)
'''
####################################################################################
'''
s = "Let's take LeetCode contest"
arr = []
for i in s.split():
	arr.append(i[::-1])
a = ""
for j in arr:
	a+=j+" "
print(str(a))
'''
##############################################################################
'''
# leetcode problem:
def problem(inp): # 16
	ac = 100
	a = inp % 10
	b = 0
	if a < 5:
		b = b + abs(inp - a)
	else:
		b = b + abs((10-a) + inp)
	print(ac - b)
problem(21)
'''
############################################################################

'''
Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
'''
'''
def sym(low,high):
	arr = []
	for i in range(low,high+1):
		if i > 10:
			s = str(i)
			h = int(len(s) / 2)
			p1 = s[0:h]
			p2 = s[h:]
			r = u = 0
			for j in p1:
				r = r + int(j)
			for k in p2:
				u = u + int(k)
			if r == u:
				arr.append(i)
	return len(arr)
	

# driver code...
print(sym(100,1782))	
'''
####################################################################################################
'''
nums = [51,71,17,24,42]
for i in range(1,len(nums),2):
	f = nums[i]
	print()
	for j in range(i+1,len(nums),2):
		g = nums[j]
		print(g)
'''
#########################################################################################
'''
arr = []
w = ["|||"]
sep = "|"
for i in w:
	for j in i.split(sep):
		if (j != ""):
			arr.append(j)
print(arr)
'''
#########################################################################################
'''		
w = "USA"
if w.isupper():
	print(True)
elif w.islower():
	print(True)
elif w.istitle():
	print(True)
else:
	print(False) 		
'''
######################################################################################
'''
# diplay leap year's in particular range...
for i in range(2000,3001):
	year = i
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		print(i)
'''
#######################################################################################
'''
# day of the year...
def dayOfYear(date):
	d = { 1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31 }
	day = []
	for i in date.split("-"):
		day.append(int(i))
	if (day[0] % 4 == 0 and day[0] % 100 != 0) or (day[0] % 400 == 0 ):
		d[2] = 29
	days = 0
	for i in range(1,day[1]):
		days += d.get(i)
	return days + day[2]
	
print(dayOfYear("2023-12-24"))
'''
#########################################################################################
'''
# first unique char in an string...
def r(s):
	for i,c in enumerate(s):
		if s.count(c) == 1:
			return i
			break
	return -1
print(r("loveleetcode"))
'''
############################################################################
'''
# reverse a number...
x = 1534236469
r = 0
y = 0
if x < 0:
	y = abs(x)
else:
	y = x
while y != 0:
	d=y%10
	r=r*10+d
	y=y//10
if x < 0:
	print(-r)
else:
	print(r)
'''
##############################################################################
'''
s ="4193 with words"
st = s.strip()
l = ["0","1","2","3","4","5","6","7","8","9","-","+"]
arr = []
x = ""
for i in st:
	if i in l:
		arr.append(i)
for j in arr:
	x = x + j
print(int(x))
'''
#############################################################################
'''
# position to insert a number in an list
nums = [1,3,5,6]
target = 7
a = 0
if target in nums:
	print(nums.index(target))
else:
	for i in nums:
		if i > target:
			a = nums.index(i)
			break
		else:
			a = len(nums)
	print(a	)	
'''	
######################################################################
'''
# Remove closed paranthesis...
s = "(((()()(()())(()()(())))))"
a = ""
for i in range(0,len(s)-1):
	if s[i] == s[i+1]:
		a = a + ""                                               																	
	else:									
		a = a + s[i] 
print(a + s[-1])
'''
#########################################################################
'''
int = 6282289928328323283293
str = "eeuheug3668392()2252362"
float = 2272.7832892
(bool == True / False)
list = [2,2,2,"dgwd","wwu",True]
set = {1,2,3,4,"apple"}
tuple = (1,3,34,4,5,5,"eeuh","ehdeu","()()()()")
dict = {1:"hello",2:"bye"}
'''
##########################################################################
'''
# [even,odd,even,odd.....]
nums = [2,3]
arr = []
f = 0
g = 1
for i in nums:
	if i % 2 == 0:
		arr.insert(f,i)
		f = f + 2
	else:
		arr.insert(g,i)
		g = g + 2
print(arr)
'''
###################################################################
'''
# zip function....
# [1,0,1,0,1,0]
a = [1,1,1]
b = [0,0,0]
arr = []
for i,j in zip(a,b):
	arr.append(i)
	arr.append(j)
print(arr)
'''
###############################################################
'''
nums = [3,2,1,5,4]
k = 2
arr = []
for i in range(0,len(nums)):
	for j in range(i+1,len(nums)):
		arr.append(abs(nums[i]-nums[j]))
print(arr.count(k))
'''
##############################################################
'''
pattern = "abba"
s = "dog cat cat dog"
'''
########################################################
'''
a = [1,2,3]
b = a
b += [4,5] # just modifying the original list...
b = b + [6,7] # list + list = new list...
print(a)
print(b)
'''
##########################################
'''
# File handling...(read)..
f = open("file.txt","r")
for z in (f.read()).split():
	print(z)
f.close() # The file had closed if we try to read it throughs an value error...
print(f.read()) 
'''
###########################################
'''
# file handling....(write...)
f = open("file.txt","a")
string = " chinna sumanth kumar shetty..."
f.write(string)
f.close()
f = open("file.txt","r")
print(f.read())
print(f.tell())
'''
#############################################
'''
# working in python os module...
import os
os.rmdir("/home/sumanth/Desktop/chinna.txt")
'''
############################################
"""
# classes,methods,objects in python...
class CreditCard:  # created a class named as CreditCard...
	''' A customer credit card...'''
	def __init__(self,customer,bank,acnt,limit): # constructor...
		''' Create a new credit card instance...'''
		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = 0
	
	def get_customer(self): # methods of CreditCard class...
		return self._customer
	def get_bank(self):
		return self._bank
	def get_account(self):
		return self._account
	def get_limit(self):
		return self._limit
	def get_balance(self):
		return self._balance
	def charge(self,price):
		if self._balance + price > self._limit: # 500 > 1000 False...
			return False
		else:
			self._balance += price
			return True
	def make_payment(self,amount):
		self._balance -= amount

cc = CreditCard('sumanth','fi','9014991769',1000) # creating an object(cc) for to a CreditCard class..
print(cc.get_customer())
print(cc.charge(500))
print(cc.get_balance()) # 0 -- 500
cc.make_payment(200)
print(cc.get_balance()) # 500 -- 300
"""
################################################
'''
# freching the elements form the sequence of list....
class Seq_Iterator:
	def __init__(self,sequence):
		self._seq = sequence
		self._k = -1
	def __next__(self):
		self._k += 1
		if self._k < len(self._seq):
			return self._seq[self._k]
		else:
			raise StopIteration()
	def __iter__(self):
		return self
sequence = [1,2]
s = Seq_Iterator(sequence)
print(s.__next__())
print(s.__next__())
'''
########################################################
'''
# Implementation of stacks...(Stack follows LIFO order...)
class Stack:
	def __init__(self):
		self.arr = []
	def push(self,element):
		self.arr.append(element)
	def pop(self):
		self.arr.pop()
	def size(self):
		return len(self.arr)
	def display(self):
		return self.arr
	def peek(self):
		return self.arr[-1]
	def maxi(self):
		return max(self.arr)
	def mini(self):
		return min(self.arr)
	def sum(self):
		return sum(self.arr)
	def search(self,element):
		return element in self.arr
	def isempty(self):
		return len(self.arr) == 0
	def clear(self):
		self.arr.clear()
# Driver code...
s = Stack()
s.push(5)	# [5]
s.push(19)	# [5,19]
s.push(7)	# [5,19,7]
s.push(9)	# [5,19,7,9]
s.push(3)	# [5,19,7,9,3]
s.pop()		# [5,19,7,9]
print(s.size())	# 4
print(s.peek())	# 9
print(s.maxi())	# 19
print(s.mini())	# 5
print(s.sum())	# 40
print(s.search(99))	# False
print(s.isempty())	# False
print(s.display())	# [5,19,7,9]
s.clear()
print(s.isempty())	# True
print(s.display())	# []	
'''
########################################################
'''
# Implementation of Queues...(Queue follows FIFO order...)
class Queue:
	def __init__(self):
		self.arr = []
	def enqueue(self,element):
		self.arr.append(element)
	def dequeue(self):
		self.arr.pop(0)
	def size(self):
		return len(self.arr)
	def display(self):
		return self.arr
	def peek(self):
		return self.arr[-1]
	def maxi(self):
		return max(self.arr)
	def mini(self):
		return min(self.arr)
	def sum(self):
		return sum(self.arr)
	def search(self,element):
		return element in self.arr
	def isempty(self):
		return len(self.arr) == 0
	def clear(self):
		self.arr.clear()
# Driver code...
q = Queue()
q.enqueue(5)	# [5]
q.enqueue(19)	# [5,19]
q.enqueue(7)	# [5,19,7]
q.enqueue(9)	# [5,19,7,9]
q.enqueue(3)	# [5,19,7,9,3]
q.dequeue()	# [19,7,9,3]
print(q.size())	# 4
print(q.peek())	# 3
print(q.maxi())	# 19
print(q.mini())	# 3
print(q.sum())	# 38
print(q.search(9))	# True
print(q.isempty())	# False
print(q.display())	# [19,7,9,3]
q.clear()
print(q.isempty())	# True
print(q.display())	# []
'''
#########################################################
'''
# Implementation of single linked list...
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)

    my_list.display()  # Output: 1 -> 2 -> 3 -> None

    my_list.prepend(0)
    my_list.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

    my_list.delete(2)
    my_list.display()  # Output: 0 -> 1 -> 3 -> None
'''
##########################################################
'''
# L.C - 506
score = [10,3,8,9,4]
d = {}
answer = []
x = sorted(score,reverse = True) # 5,4,3,2,1
for i in range(len(x)):
	if i == 0:
		d[x[i]] = "Gold Medal"
	elif i == 1:
		d[x[i]] = "Silver Medal"
	elif i == 2:
		d[x[i]] = "Bronze Medal"
	else:
		d[x[i]] = str(i+1)
for i in score:
	answer.append(d[i])
print(answer)
'''
#############################################################
'''
# L.C - 561	
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        t = 0
        nums.sort()
        for i in range(len(nums)):
            if(i+1)%2 == 1:
                t += nums[i]
        return t
'''
###################################################
# 888
# 88
############################################
'''
# l.c - 151
s = "the sky is blue"
arr = list(s.split())
r = ""
for i in reversed(arr):
	r += i + " "
print(r[:-1])
'''
####################################
'''
# l.c - 238
nums = [1,2,3,4]
r_arr = []
e = 1
for i in range(len(nums)):
	nums.pop(nums[i])
	for j in nums:
		e *= j
	r_arr.append(e)
print(r_arr)
		
'''
################################################
'''
# 2824
nums = [-1,1,2,3,1]
nums.sort()
target = 2
count = 0
'''
################################
'''
smart bus pass system using andriod(revolutionizing public transportation...)

https://linuxhint.com/install_android_studio_ubuntu/

/home/sumanth/AndroidStudioProjects/FirstApp
'''
####################################################################
'''
# 125(l-c)
a = "madam	"
s = ""
for i in a:
	if i.isalpha(): s+=i
print(s.lower() == s.lower()[::-1])
'''
###################################################################
'''
ops = ["5","-2","4","C","D","9","+","+"]
out = []
x = 0
for i in ops:
	if i.isdigit():
		out.append(int(i))
	elif i == 'C':
		x = out.pop()
	elif i == 'D':
		out.append(int(x) * int(out[-1]))
	elif i == '+':
		out.append(int(out[-2]) + int(out[-1]))
print(out)
ans = 0
for i in out:
	ans += i
print(ans)
'''
########################################################
'''
# binary search...

list--sort--increasing order...
mid -- by length // 2...

def b_s(l,target):
	l.sort()
	low = 0
	high = len(l)-1
	while low <= high:
		mid = (low + high)//2
		m_v = l[mid]
		if m_v == target:
			return ("element found at index : ",mid)
		elif m_v < target:
			low = mid + 1
		else:
			high = mid - 1
print()
# driver code...
l = [3,2,4,6,8,9,1]
target = 9
print(sorted(l))
print(b_s(l,target))
'''

##################################################################################
'''
# 2269 l.c
nums = "430043" # 0:2  2:4  4:6
k = 2
b = 0
for i in range(0,len(nums)-1):
	try:
		if int(nums) % int(nums[i:i+k]) == 0:
			b += 1
	except Exception:
		pass
print(b)
'''
#############################################################################
'''
# 509 

def f(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return f(n-1) + f(n-2) 



# driver code...
n = 4
print(f(n))
'''
################################################################################		
'''
s = "xyzzaz"
c = 0
for i in range(len(s)-2):
	r = set(s[i:i+3])
	if len(r) == 3:
		c += 1
print(c)
'''
################################################################################
'''
# 1984
nums = [9,4,1,7]
k = 2
if len(nums)<=1:
	return 0
nums.sort()
d = float('inf')
for i in range(len(nums)-k+1):
	diff = abs(nums[i] - nums[i+k-1])
	d = min(diff,d)
return d
'''
##############################################################################
'''
# 713
nums = [10,5,2,6]
k = 100
if k<=1:
	return 0
left = ans = 0
curr = 1
for right in range(len(nums)):
	curr *= nums[right]
	while curr = k:
		curr //= nums[left]
		left += 1
	ans += (right - left + 1)
return ans
'''
###########################################################################

########################################################################################
'''
def rats(r,unit,n,arr):
	t = 0
	c = (r*unit)
	for i in range(1,n):
		t += arr[i]
		if t >= c:
			return i
			break
# driver code...		
r = 2
unit = 7
n = 8
arr = [2,3,4,5,6,7,8,9]
print(rats(r,unit,n,arr))
'''
#########################################################################################

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next_node
            return

        current = self.head
        while current.next_node and current.next_node.data != data:
            current = current.next_node

        if current.next_node:
            current.next_node = current.next_node.next_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next_node
        print("None") 

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
linked_list.display()
linked_list.delete(2)
linked_list.display()
'''
########################################################################################
'''
def string(s,t):
	if len(s) != len(t):
		return False
	else:
		for i in range(len(s)):
			if(s.count(s[i]) == t.count(t[i])):
				return 1
			else:
				return 0
				

# driver code....
s = "foo"
t = "bar"
print(string(s,t))
'''	
#######################################################################################
'''
# Divide and conquer technique...
# Binary Search

class DC:
	def Sort(b):
		# sort the elements in the list by Ascending order...
		for a in range(1,len(b)):
			for c in range(0,len(b)-1):
				if b[c] > b[a]:
					b[c],b[a] = b[a],b[c]
		# the elements had sorted in non decreasing order...
		return b
	
	def Search(self,b,target):
		b = DC.Sort(b)
		low = 0
		high = len(b)
		try:
			while high >= low:
				mid = (low + high)//2
				if b[mid] == target:
					return (f"The element found at index {mid}")
					break
				elif b[mid] < target:
					low = mid + 1
				else:
					high = mid - 1
		except Exception:
			return (f"The element not found in the above list..")
			

# Driver code....
b = [2,1,3,4,5,7,9,0,6]
target = 7
R = DC()
print(R.Search(b,target))
'''
######################################################################################################
'''
# factorial
class Factorial:
	def __init__(self):
		self.n = n
	def fact(self,n):
		fact = 1
		for i in range(1,n+1):
			fact = fact * i	
		return fact
# driver code....
n = int(input("Enter a number : "))
F = Factorial()
print(F.fact(n))
'''
#####################################################################################################
'''
# visual --- using matplotlib...
from matplotlib import pyplot as plt
x = [1,2,3]
y = [4,5,6]
plt.bar(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("plot")
plt.grid()
plt.show()
'''
###################################################################################################
'''
# Array
arr = []
arr.append(5)
arr.append(19)
arr.append(7)
arr.append(9)
print(arr[::-1])
'''
################################################################################################
'''
a = [16,17,4,3,5,2]
r = []
for i in range(len(a)-1):
	if a[i] < a[i+1]:
		r.append(a[i+1])
r.append(a[-1])
print(r)
'''
#########################################################################################
'''
# implementation of linked list.....
class Linked_List:
	def __init__(self,value,nextNode = None):
		self.value = value
		self.nextNode = nextNode
node1 = Linked_List("5")
node2 = Linked_List("19")
node3 = Linked_List("7")
node4 = Linked_List("9")

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
# 5 -> 19 -> 7

currentnode = node1
while True:
	print(currentnode.value, end=" -> ")
	if currentnode.nextNode is None:
		print("None")
		break
	currentnode = currentnode.nextNode			
'''
###########################################################################################
'''
# Linked list.......in DSA...
class Linked_List_Node:
	def __init__(self, value, nextNode = None):
		self.value = value
		self.nextNode = nextNode
class LinkedList:
	def __init__(self,head = None):
		self.head = head
	def insert(self, value):
		node = Linked_List_Node(value)
		if self.head is None:
			self.head = node
			return
		currentNode = self.head
		while True:
			if currentNode.nextNode is None:
				currentNode.nextNode = node
				break
			currentNode = currentNode.nextNode	
	def printList(self):
		currentNode = self.head
		while currentNode is not None:
			print(currentNode.value, end = " -> ")
			currentNode = currentNode.nextNode
		print("None")
	def listSum(self):
		add = 0
		currentNode = self.head
		while currentNode is not None:
			add = add + currentNode.value
			currentNode = currentNode.nextNode
		print(add)
	def isEmpty(self):
		if self.head is None:
			print("emply list")
		else:
			print("not empty")

	def deleteElements(self,value):
		if self.head.value == value:
			self.head = self.head.nextNode
		currentNode = self.head
		while currentNode.nextNode and currentNode.nextNode.value != value:
			currentNode = currentNode.nextNode
		if currentNode.nextNode:
			currentNode.nextNode = currentNode.nextNode.nextNode	
			
# Driver code.....	
l = LinkedList()   # 5 ->  7 ->  9 -> 19 -> None
l.insert(5)
l.printList()
l.insert(7)
l.insert(9)
l.insert(19)
l.printList()
l.listSum()
l.isEmpty()
l.deleteElements(7)
l.printList()
'''
################################################################################################
'''
# iterating the generator....
d = (x for x in range(10))
while True:
	try:
		print(d.__next__())
	except Exception:
		break
'''
################################################################################################




	








































	





















































































































