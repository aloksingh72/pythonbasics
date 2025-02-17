# Dated:->17/02/2025/Monday
# OOPs concept 
# four pillars of object oriented programming:
                                        # 1.Abstraction
                                        # 2.Encapsulation
                                        # 3.Inheritance
                                        # 4. Polymorphism
# python Inheritance
# creating a parent class

"""
    ::->___init__() function is invoked at the time of object creation
    python will automatically create a constrctor init if we don't create it manually
    ::->self holds the  reference  to  the  current object  that is created, and it is used to access the 
    variables that belongs to that class.


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


"""
class Student:
    college="ABC college University"
    name  = "anonymous"
    
    def __init__(self,fname,lname):
        self.name = fname
        self.lastname = lname
        print("adding the student in Database...")
    
    # Atribute of class(properties)
    def __init__(self,name,lname,marks):
        self.name = name
        self.lname = lname 
        self.marks = marks
     # method functions of class
    def welcome(self):
        print("welcome studente,",self.name)   


s1 = Student("Karan","Singh",72)
print(s1.name)
s1.welcome()

print(s1.name)
print(s1.lname)
print(s1.marks)
print(s1.name,s1.lname,s1.marks)
"""

# question:- make a class student and a constructor that takes a name and 3 subject  marks and finds the average of those marks
"""
class Student:
    def __init__(self,name,marks):
        self.name = name 
        # self.marks1 = marks1
        # self.marks2 = marks2
        # self.marks3 = marks3
        self.marks = marks

    def average(self):
        # avg = (self.marks1+self.marks2+self.marks3)/3
        # print("the aversge of marks is",avg)
        sum = 0
        for val in self.marks:
            sum += val
        print("hi ",self.name,"your average is",sum/3)
        
# creating the object of class students
p = Student("karan",[25,45,89])
p.average()
p.name = "Tony stark"
p.average()
"""

# Static methods 
# are those method that don't use the self as a  parameters
"""
class Student:
    # this is called decorator it extend the behaviour of the wrapped function, without this method static nhi banega
    @staticmethod
    def college():
        print("hello College")

p = Student()
p.college()

"""

# four Pillars of OOPs
# Abstraction:- Hiding the implementation details of a class and only showing the essential features to the users
# Encapsulation:- Wrapping data and functions into a single unit(object)
