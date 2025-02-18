# pattern program
"""

n =5
for i in range(1,n+1):
    # for spaces
    for j in range(n-i):
        print(" ",end="")
    # for stars
    for j in range(i):
        print("* ",end="")
    print()

    # lower part
for i in range(n-1,0,-1):
    # for spaces
    for j in range(n-i):
        print(" ",end="")
    # for stars
    for j in range(i):
        print("* ",end="")
    print()
"""

n =5
# upper part
for i in range(1,n+1):
    # for spaces
    for j in range(n-i):
        print(" ",end="")
     # for stars
    for j in range(i):
        print("* ",end="") 
    print()

# lower part
for i in range(n-1,0,-1):
    # for spaces
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    print()
 

       
    
    