# Python if else 
"""
a= 23
b = 67
if a > b:
	print("a is the greatest one")
else:
	print("b is the greatest one")
"""

#elif statement
"""
a = 72
b = 72
if a > b :
	print("a is the greatest one")
elif a == b:
	print(" both are equal")
"""
#else statement
"""
a = 72
b = 82
if a > b :
	print("a is the greatest one")
elif a == b:
	print(" both are equal")
else:
	print("b is the greatest one")
"""


#Shorthand if statement
"""
a = 34
b = 86
print("A") if a > b else print("B")
"""

#one line if else statement with 3 statement
"""
a = 330
b = 340

print("A") if a > b else print("=") if  a== b else print("B")
"""
"""
a= 200
b = 89
c = 78
if a>b and b > c :
	 print("A is the greatest")
 
"""
# OR statement
"""
a = 45
b = 89
c =78
if a>b or b>c :
	print("at least one of the condition is true")

"""
# nested if
"""
x =40
if x>10:
	print("above 10")
	if x >20:
		print("also above 20")
	else:
		print("not above 20")

"""
#python loops 
#python have two primitive loop command 
#1.while loops
#2.for loops
"""
i =1
while i<=10:
	print(i)
	i +=1
"""

# break statement
# it will break the loop even the condition is true
"""
i =1
while i<10:
	print(i)
	if i == 3:
		break
	i +=1

"""
#continue statement
"""
i =0
while i <6:
	i +=1
	if i ==3:
		continue
	print(i)
"""

#Looping through the strings
"""
for x in "Banana":
	print(x)
"""
#break statement in for loop
"""
fruits  = ["apple","banana","oranges"]
for x in fruits:
	print(x)
	if x == "banana":
		break
"""
#continue statement in for loop
"""
fruits  = ["apple","banana","oranges"]
for x in fruits :
	if x == "banana":
		continue
	print(x)
"""
#range() function 
# range function returns a sequence  of numbers starting form 0 by default and step value is 1
"""
for x in range(6):
	print(x)
"""
# we can modify the range function

"""
for x in range(3,30,3):
	print(x)
"""
"""

for x in range(3,30,3):
	print(x)
else:
	print("FInally finsihed...")
"""
# Nested loops
"""
adj = ["red","orange","yellow"]
fruits = ["apple","oranges","magoes"]
"""
# for one times of outer loops the inner loops 
"""
for x in  adj:
	for y in fruits:
			print(x,y)
"""
# --------------------------------Python Functions-------------------
""""
# function decalarations
def my_function():
    print("hello this my function")

# function calling
my_function()
"""

# Arguments in a functions
"""

def my_function(myname):
    print(myname,"the name as argruments")
    
my_function("alex")
my_function("linux")
"""

"""

def my_function2(firstname,lastname):
    print("name of the candidate is ",firstname,lastname)

my_function2("alex","solly")
"""

# Arbitrary Arguments, *args
# if we don't know the actual no. of arguments we have to use the *args parameter
"""

def my_function3(*kids):
    print("the youngest kids is ",kids[2])
    
my_function3("linux","alex","jack","john doe")
""" 

# Arbitrary keywords Arguments, **args
# You can also send arguments with the key = value syntax

"""

def my_function4(**kid):
	print("the last name is",kid["lname"])

my_function4(fname= "alex",lname= "singh")
"""


# default Parameter value
"""

def my_function5 (mycountry = "India"):
	print("my country is "+mycountry)

my_function5("Ireland")
my_function5("Nepal")
my_function5()
"""


# sending the list as arguments to the functions

"""

def my_function6(fruits):
	for x in fruits:
		print(x)

food = ["apple","orange","grapes"]
my_function6(food)
"""

# return statements

"""

def my_function7(value):
    return 5*value

print(my_function7(5))
"""

# Python Lambda functions
# A lambda function in Python is a small, anonymous function defined with the lambda keyword instead of the usual def keyword. 
# It allows you to write quick functions in a single line without formally naming them.
"""
square = lambda x: x*x
print(square(4))

add_lambda = lambda x,y:x+y
print(add_lambda(4,5))

"""
#Array in Python
# creating an array
"""

car = ["Ford","BMW","Honda","Audi","Ford"]
x = car[1]
car[1] = "Range Rover"
y = car[1]
print(x)
print(y)
print(len(car))
for x in car:
    print(x)
# pop() mehthod
car.pop(3)
print(car)
# remove() method:- it will remove the first occurence of the items
car.remove("Ford")
print(car)
"""


# ----------------------Python Classes and Objects----------------------
# create the class
"""
class MyClass:
    x = 5

p1 = MyClass()
# we can't directly print the value of x without making the object 
print(p1.x)
"""

# _int()_ function :- to assign the value to object properties


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("John",24)
print(p1.name)
print(p1.age)



#__str__() function :-readable string representation of the object.

"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
   		 return f"Person(Name:{self.name},Age:{self.age})" 
		
# creating the object
person1 = Person("ALice",30)
print(person1)
"""