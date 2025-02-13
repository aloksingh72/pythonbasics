#Write a Python program to reverse a list using different approaches


#using built-in reverse() methods 
"""
def reverselist(lst):
	lst.reverse()
lst = [1,2,3,4,5,6]
print(lst)
"""
#using slicing
"""
def reverseslice(lst):
	return lst[::-1]

lst = [1,2,3,4,5,6]
slicedlst = reverseslice(lst)
print("original list",lst)
print("Reverse list",slicedlst)
"""

#using loop
def reverselst(lst):
	left =0
	right = len(lst)-1
	while left < right:
		lst[left],lst[right] = lst[right],lst[left]
		left = left+1
		right = right-1
	

lst = [1,2,3,4,5,6,7]
print("original list",lst)
reverselst(lst)

print("reversed list",lst)






