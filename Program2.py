# taking the user input


# Program 1 to search the number of occurences in the list
"""
n = int(input("Enter the value to be search..."))
numbers = [1,1,1,2,2,3,3,8,8,8,9,9]

occurence = 0

for nums in numbers:
        if nums == n:
            occurence +=1
print(f"the number {n} is found {occurence} times")
"""


numbers = [1,1,2,2,2,3,3,8,8,8,9,9]
occurence = {

}
# without using the get method 
for nums in numbers:
    if nums not in occurence:
      occurence[nums] = 1
    else:
       occurence[nums] += 1

# with using the get method  
#    occurence[num = occurence.get(nums,0) + 1

print(occurence)











