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
"""
class Car:
    def __init__(self):
        self.acc = False
        self.brak= False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started...")

car1 = Car()
car1.start()
"""

# Encapsulation:- Wrapping data and functions into a single unit(object)

# Questions:- create the caccount class  with 2 attributes - balance & account no. 
#         create methods for debit, credit & printing the balance.
"""
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc
    # debit methods
    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ",self.get_balance())
    # credit methods
    def credit(self , amount):
        self.balance += amount
        print("Rs.",amount,"was credited...")
        print("total balance = ", self.get_balance())
    def get_balance(self):
        return self.balance

acc1 = Account(100,123)
acc1.debit(40)
acc1.credit(20)
acc1.credit(20)
"""

# del keyword
# used to delete object properties or object itself
# del s1.name  :- for deleting the particular member inside that object
# del s1  for completely deleting the object

"""
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Mohan")
print(s1.name)
del s1.name
print(s1.name)
"""
# private entity in object oriented programming language
# for doing private we have to use __ (double underscore)
# Private attributes  & methods are meant to be used only within the class and are not accessible from outside the class.

"""
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345","abc")
print(acc1.acc_no)
# print(acc1.__acc_pass)
acc1.reset_pass()

"""
# Inheritance 
#  When one class(child/derived) derives the properties & methods of another class (parent/base)
"""
class Car:
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
    
car1 = ToyotaCar("Fortuner")
car2  = ToyotaCar("pirus")

print(car1.start())
print(car1.name)
"""
# inheritance is of three types:
                # 1. Single Inheritance
                # 2.Multi-level Inheritance
                # 3.Multiple Inheritance
# example of multi-level inheritance 
"""
class Car:
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand
    
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()

"""
# example of mutiple inheritance
"""
class A:
    varA = "Welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)

"""

# Super method 
# is used to access methods of the parent class.
"""
class Car:

    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()
    


car1 = ToyotaCar("diesel","electric")
print(car1.type)
"""
# classmethod decorator 
# have to study

#@property method
# makes a  method behaves like an attribute 

"""
class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy +self.chem + self.math) / 3) +"%"
    
stu1 = Student(98,78,56)
print(stu1.percentage)

stu1.phy = 75
print(stu1.percentage)
"""

#Polymorphism   
# Operator overloading 
# when the smame 
print(1+2)
print(type(1))
print("alok"+"singh")
print(type("alok"))
print([1,2,3]+[7,8,9,])
print(type([1,2,3,5]))
