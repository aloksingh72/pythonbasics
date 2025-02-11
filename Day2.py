#Dated-> 11/02/2025/Tuesday

#Python casting
#Casting in python is therefore done using constructor functions.
#int()
#float()
#str()
"""
x= int(1)
y =int(3.7)
z= int("3")

print(x)
print(y)
print(z)

"""

"""
x= float(1)
y= float("3")
z= float("4.3")

print(x)
print(y)
print(z)
"""

#python Strings

print("hello")
print('hello')

#quotes inside quotes

print("I am 'running'")
print('he is "playing"')

#multi line Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)


# Strings Slicing

a= "Hello world!"

print(a[2:5])

b = "Hello, World!"
print(b[-5:-2])

#NOTE:- txt.strip() is used to reduce the whitespaces form begining and ending

txt =" hello world "
print(txt)
print(txt.strip())

#String concatenation


a= "hello world!"
b= "Hello python"

print(a+b)
print(a+" "+b)
#  F-String to combine the string and numbers

price=1
txt = f"The price is {price} dollars"

print(txt)

txt = f"the updated value of dollars in rupees {price*80}"
print(txt)

#Escape character 
print(" we are so-called \"Vikings\" from the north")


#Strings Method
#Python has a set of built-in methods that you can use on strings
#Note:- All string methods return new values. They do not change the original string.

str1= "happy coding"
print(str1.isprintable())

str2 = "hello python"
print(str2.isupper())

str3 = "namaste world"
str4 = "namaste python"

print("#".join(str4))

print(str1.upper())

"""
#boolean operator 
a= 10
b= 34
if b>a:
    print("b is the greatest number")

else:
    print("a is the greatest number")
"""
    
"""
x= 200
print(isinstance(x,int))

print((6+3)-(4-5))


#List in python
# it is used to multiple items in a single variable
thisislist = ["banana","apple","orange"]
print(thisislist)
print(len(thisislist))


#the list may contains different  datatypes
list1 = ["abc",34,True,"hello world"]
print(list1)



#updating the list items
thislist = ["apple","backcurrant","grapes","hello world"]
thislist[3] = "mango"
print(thislist)

#updating the range of items
thislist2 = ["apple","backcurrant","grapes","hello world"]
thislist2[1:2] = ["watermelon","mangoes"]
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
thislist3[1:3] = ["watermelon"]
print(thislist3)

thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist4[1:3] = ["blackcurrant", "watermelon"]
print(thislist4)

"""
#append the list items
#append() method
thislist5=["apple", "banana", "cherry", "orange"]
thislist5.append("mangoes")
print(thislist5)

# inserting the items into the list
#insert() method
thislist6 = ["mango","apple","cherry"]
thislist6.insert(2,"watermelon")
print(thislist6)

#Extend() method 
thislist7 = ["winter","summer","rainy"]
addseason = ["spring"]
thislist7.extend(addseason)
print(thislist7)

#remove() method
thislist8 = ["winter","summer","rainy"]
thislist8.remove("winter")
print(thislist8)

#pop() method
thislist9 = ["winter","summer","rainy","spring"]
thislist9.pop(1)
print(thislist9)

#del() method
thislist10 = ["winter","spring"]
del thislist10[1]
print(thislist10)

#clear() method
thislist11 = ["summer","rainy","spring","winter"]
thislist11.clear()
print(thislist11)






