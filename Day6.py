# Dated:->17/02/2025/Monday
# python Inheritance
# creating a parent class

"""
    ___init__() function is invoked at the time of object creation
    python will automatically create a constrctor init if we don't create it manually
    ::->self holds the  refer of the  object that is created 

"""
"""
class Person:
    # __init__() function is a constructor that is used to initialize the values of the objects
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname,self.lastname)

x = Person("Alex","Doe")
x.printname()
"""
class Student:
    name  = "Karan"
    def __init__(self,fname):
        self.name = fname
        print("adding the student in Database...")


s1 = Student("Karan")
print(s1)
print(s1.name)

