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

# Module keywords
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
import platform
x = dir(platform)
y = platform.processor()
z =platform.uname()
print(y)
print(z)

