#Loop through a List

"""
thislist1 = ["apple","banana","cherry"]
for x in thislist1:
	print(x)
"""
"""
#loop through the index number
thislist2 = ["apple","banana","cherry"]
for i in range (len(thislist2)):
	print(thislist2[i])

"""
"""
#loop through the while loop
thislist3 = ["apple","banana","cherry","mangoes"]
i=0
while i < len(thislist3):
	print(thislist3[i])
	i= i+1
"""

"""
#looping using list comprehension

thislist4 = ["apple","banana","cherry","mangoes"]
[print(x) for x in thislist4]
"""

#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

"""
fruits = ["apple","oranges","mangoes","cherry","blackcurrant"]
newlist = []

for x in fruits:
	if "o" in x:
		newlist.append(x)
print(newlist)
"""


"""
#using list comprehension shortand the lines of code

fruits2 = ["apple","oranges","mangoes","cherry","blackcurrant"]
newlist = [x for x in fruits2 if "o" in x]
print(newlist)	
"""
"""
fruits3 = ["apple","oranges","mangoes","cherry","blackcurrant"]
newlist = [x for x in fruits3 if x!= "apple"]

print(newlist)
"""

"""
fruits4 = ["apple","banana","mangoes","cherry","blackcurrant"]
newlist = [x if x != "banana" else "orange" for x in fruits4]

print(newlist)

"""
#Sort the List alphabetically
"""
thislist5 = ["banana","mangoes","cherry","apple"]
thislist5.sort()
print(thislist5)

thislist6 = [100,59,45,74,32,7]
thislist6.sort()
print(thislist6)
"""

# To sort the list in reverse order
"""
thislist7 = ["banana","mangoes","cherry","apple"]
thislist7.sort(reverse = True)
print(thislist7)

thislist8 = [100,59,45,74,32,7]
thislist8.sort(reverse = True)
print(thislist8)
"""

#Customize Sort function
"""
def myfunc(n):
	return abs(n-50)
thislist8 = [50,60,70,80,90]
thislist8.sort(key = myfunc)
print(thislist8)
"""

#Case sensitive sorting
thislist9 = ["banana","Orange","Kiwi","cherry"]
thislist9.sort()
print(thislist9)

thislist10 = ["banana","Orange","Kiwi","cherry"]
thislist10.sort(key = str.lower)
print(thislist10)

#Copy a List



