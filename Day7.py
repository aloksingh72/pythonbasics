# Dated->18/02/2025/Tuesday
# Python Polymorphism
# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.


# here len is used as many forms with different data types
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))


str1 = "model"
print(len(str1))
"""
# Sccope in Python
# local scope
"""
def myfunc():
    x = 300
    def innerfunc():
        print(x)
    innerfunc()
myfunc()
"""
# global scope
"""
x =200
def myfunc2():
    def innerfunc2():
            x =300
            print(x)
    innerfunc2()
myfunc2()
print(x)
"""


# Global keywords
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

"""
def myfunc3():
    global x 
    x =300
    def myfunc4():
        x =700
        print(x)
    myfunc4()
myfunc3()
print(x)
"""
# to change the global variable  used the keyword global inside the inner function

"""
x = 400
def func4():
    global x
    x =300
func4()
print(x)
"""

# nonlocal keyword is used to make the variable belong to the outer function
"""
def myfunc5():
    x = "Jane"
    def innerfunc5():
        nonlocal x 
        x = "alex"
    innerfunc5()
    return x
print(myfunc5())
"""

# ----------------------------->Module keywords
"""
import platform

x = platform.system()
print(x)
"""
# Note: When using a function from a module, use the syntax: module_name.function_name.

"""
import module1
module1.greetingname("Alok")
"""
"""
import module1
a= module1.person1["age"]
print(a)
# if we want to access the mutiple dictionary items
keys = ["name","age","city"] 
x = list(map(module1.person1.get,keys))
print(x)
"""

# Using the dir() Function
"""
import platform
x = dir(platform)
y = platform.processor()
z =platform.uname()
print(y)
print(z)
"""
"""
import datetime
x = datetime.datetime.now()
print(x)
"""
# strftime is used to format dates in readable format 
"""
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

"""
# ---------------------------------->Python Maths
"""
 
x = (3,6,8)
print(max(x))

a = abs(-34.56)
print(a)

# power functions
res = pow(4,3)
print(res)

import math
x = math.pi
print(x)

"""

# ----------------->Python JSON
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.


# ----converting form json to python string
# we use loads method
"""
import json
# some JSON:
x = '{"name":"Alex", "age":30, "city":"Mumbai"}'

# parsing the x 
y =json.loads(x)

print(y["name"])
print(y["age"])
print(y["city"])
"""

# -----> converting from python to json format
# we use the dumps method
"""

import json
# a python object
x = {
    "name": "Alex",
    "branch":"C.S.E",
    "year":2025

}
# convert from pytho to json 
y = json.dumps(x)
# the result is json string
print(y)
""" 

""""

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
"""

"""
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=2))
"""
#-------> RegEx Module

"""
import re
txt = "This is a new  India"
x = re.search("^This.*India$",txt)

txt = "The rain in Spain"
y = re.findall("ai", txt)

txt = "The rain in Spain"
z = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
print(x)
print(y)
print(z)
"""
# -----> Python PIP
# PIP is a package manager for Python packages
# It install the packages inside the python directory



# ----> Exception Handling----
""""
try:
    print(x)
except:
    print("this will catch an excception")
"""

"""

try:
    x=9
    print(x/0)

except NameError:
    print("variable x is not defined")
except:
    print("this will catch an exception")
"""
# if no error is raised then else block will be executed

"""

try:
    print("hello")
except:
    print("this will catch an exception")
else:
    print("nothing went wrong")
"""

# finally block will be executed wheather the exception occur or not
"""
try:
    print(x)
except:
    print("this will catch an exception")
finally:
    print("this is finally block")
"""

"""
x = -1
if x<0:
    raise Exception("x can't be negative")
"""

"""
x = "hello"
if not type(x) is int:
    raise TypeError("x must be an integer ")
"""

"""
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)
"""


# Decorators: 
# A decorator in Python is a function that modifies the behavior of another function without changing its code.
#  It is commonly used for logging, authentication, and more.

# Example1
"""

def my_decorator(func):
    def wrapper():
        print("before the function runs")
        func()
        print("after the functions runs")
    return wrapper

@my_decorator # using the decorator function
def say_hello():
    print("hello world!")


say_hello()
"""
# Example 2
"""
def greet_decorator(func):
    def wrapper(name):
        print("Greeting starts...")
        func(name)
        print("Greeting ends...")
    return wrapper


@greet_decorator
def greet(name):
    print(f"Hello,{name}!")

greet("Alok Singh")

"""
# Generators: 
# A generator is a special type of function that returns values one at a time using the yield keyword instead of returning everything at once.
# This helps in saving memory when dealing with large data.
"""
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
"""
# even number program using yield keywords 
def even_numbers(n):
    for  i in range(2 ,n+1,2):
        yield i 
    
gen = even_numbers(10)
for nums in gen:
    print(nums)    
#Day7 signing off
