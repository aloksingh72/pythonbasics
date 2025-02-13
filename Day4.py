
#Dated ->13/02/2025
#change the values of the tuples 
#Directly we can't change the values of tuples 
#So to do that firstly we convert the tuples into list and modify it and convert back to list 
"""
thislist1 = ("apple", "banana", "cherry")
y = list(thislist1)
y[1] = "kiwi"
x = tuple(y)

print(x)
"""

#using append() memthod
"""
thislist2= ("apple","cherry","mangoes")
y = list(thislist2)
y.append("orange")
thislist2 = tuple(y)
print(thislist2)
"""

#add tuple to a tuple
"""
thistuple3 = ("apple","cherry","blueberry","orange")
y = ("mangoes",)
thistuple3 += y 

print(thistuple3)
 
"""
#remove the items from the tuples
"""
thistuple4 =  ("apple","cherry","blueberry","orange")
y = list(thistuple4)
y.remove("apple")
thistuple4 = tuple(y)

print(thistuple4)
"""

#packing and unpacking of tuples
#when we assign a value to a tuples is called packing a tuples
# excating the items form it is called unpacking of the tuples

"""
fruits1 = ("apple","cherry","blueberry","orange")
(red, green,*blue)= fruits1

print(green)
print(red)
print(blue)
"""
#looping through the tuples
# using for loop
"""
thistuple5 = ("apple","banana","mangoes")
for x in thistuple5:
	print(x)
"""
"""

thistuple6 = ("apple","banana","mangoes","cherry")
i =0
while i < len(thistuple6):
	print(thistuple6[i])
	i =i+1
"""

# join the two tuples
"""
thistuple7 = ("a","b","c")
thistuple8 = ("1","2","3")

thistuple9 = thistuple7 + thistuple8
print(thistuple9)
"""


"""
fruits = ("apple","banana","cherry")
mynewtuple = fruits*2
print(mynewtuple)
"""

# tuples have two mehtod in it
# 1.count() :- how many times a specifed items
"""
fruits = ("apple","banana","cherry","apple","apple")
x = fruits.count("apple")
print(x)
"""

#2.index():-searches the index of the items int he tuples

"""
fruits2 = ("apple","banana","cherry","apple","apple")
x1 = fruits2.index("banana")
print(x1)
"""

#PYTHON SETS

# A set is a collection which is unordered, unchangeable*, and unindexed.
"""
thisset1 = {"apple","banana","cherry","apple"}
print(thisset1)
# duplicate values are ignored
thisset2 = {True,1,False,0}
print(thisset2)
"""

# finding the length of the set


"""
thisset3={"apple","banana","cherry","grapes"}
result = len(thisset3)
print(result)
"""


"""
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
"""
# type() mehtod of set return an object with class set
"""

thisset3={"apple","banana","cherry","grapes"}
print(type(thisset3))
"""

#accessing items from the set
"""
thisset4 = {"apple","banana","cherry","grapes"}
for x in thisset4:
    print(x)
"""
#Change items in the set
#Once a set is created, we cannot change its items, but you can add new items

#adding new items in the set
#using the add() method
"""
thisset5 = {"apple","banana","cherry","grapes"}
thisset5.add("oranges")
print(thisset5)
"""
#update() method to add items form another set to current set
"""
thisset6 = {"apple","banana","cherry","grapes"}
thisset7 = {"winter","spring","summer"}
thisset6.update(thisset7)
print(thisset6)
"""

#remove() method to remove items from the set
#Note if items not exits it will raise an error
"""
thisset8 = {"apple","banana","cherry","grapes"}
thisset8.remove("banana")
print(thisset8)
"""

# discard() method to remove items form the set but it will not raise an error if items is not exists
"""
thisset9 = {"apple","banana","cherry","grapes"}
thisset9.discard("oranges")
print(thisset9)
"""

#pop() method to remove items form the set
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.


"""
thisset10 = {"apple","banana","cherry","grapes"}
x = thisset10.pop()
print(x)
"""

#looping through the set

"""
thisset11 = {"apple","banana","cherry","grapes"}
for x in thisset11:
    print(x)
"""

#join the set
# union() method 
"""
set1 = {"1","2","3"}
set2 = {"a","b","c"}
set3 = set1.union(set2)
print(set3)
"""


#join the multiple set together
"""
set3 = {"1","2","3"}
set4 = {"a","b","c"}
set5 = {"apple","mangoes","orange"}
set6 = {"blue","green","yellow"}

# set7 = set3.union(set4,set5,set6)
set7 = set3 | set4 | set5 | set6
print(set7)
"""

#intersection method
"""

set8 = {"apple", "banana", "cherry"}
set9 = {"google", "microsoft", "apple"}
# set10 = set8.intersection(set9)
set10 = set8 & set9
print(set10)
"""
#intersection_update() method change the original set instead of updatingn the returnin the new set
"""

set11 = {"apple", "banana", "cherry"}
set12= {"google", "microsoft", "apple"}
set11.intersection_update(set12)
print(set11)
"""

#difference () method
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

"""
set12 = {"apple", "banana", "cherry"}
set13 = {"google", "microsoft", "apple"}
# set14 = set12.difference(set13)
set14= set12 - set13
print(set14)
"""

#Python Dictionaries
# used to store data values in key:value pairs
"""
thisdic1 = {
    "brand":"Ford",
    "model":"mustang",
    "year":1984,
    "year":1984
}

print(thisdic1)
print(type(thisdic1))
print(thisdic1["model"])
#also can be done with get() method 
print(thisdic1.get("brand"))
# keys() method return the list of all the keys
print(thisdic1.keys())
"""
"""

x = thisdic1.keys()
print(x)

thisdic1["color"]="white" 
print(x)
print(thisdic1.values())
"""
"""
thisdic2 = {
    "brand":"Ford",
    "model":"mustang",
    "year":1984,
    "color":"black"
}

x = thisdic2.values()
print(x)#before the changes
thisdic2["color"] = "white"
print(x)
"""

# to check the presence of the specific keys

"""

if "model" in thisdic2:
    print("Model is present in this dictionary")
else:
    print("Model is not present in this dictionary")
"""

"""
#update the dictionary 
thisdict3 = {
    "brand":"fortuner",
    "model":"legender",
    "year":2024
}
#when we use the update we have to write within the ({})
thisdict3["year"] =2025 
print(thisdict3)
thisdict3.update({"model":"s3"})
print(thisdict3)

thisdict3["color"] = "white"
print(thisdict3)
thisdict3.update({"color":"black"})
print(thisdict3)

thisdict3.pop("model")
print(thisdict3)

thisdict3.clear()
print(thisdict3)
"""
"""
thisdic4 = {
    "brand":"Ford",
    "model":"mustang",
    "year":1984,
    "color":"black"
}

for x in thisdic4:
    print(x)
for y in thisdic4:
    print(thisdic4[y])
"""
"""
for x,y in thisdic4.items():
    print(x,y)
"""
#copy the dictionary
"""
thisdict5 = {
    "brand":"Ford",
    "model":"mustang",
    "year":1984,
    "color":"black"
}
"""
#using the copy() method 
"""
copydict = thisdict5.copy()
print(copydict)
"""
#using the dict() function
"""
copydic2 = dict(thisdict5)
print(copydict)
"""

#Nested dictionary :- dictionary inside another dictionary
myfamily = {
    "child1":{
        "name":"alex",
        "age":21
    },
    "child2":{
        "name":"alice",
        "age":25
    },
    "child3":{
        "name":"Linus",
        "age":26
    }
}

#Accessing items in the nested dictionary
print(myfamily["child2"]["name"])