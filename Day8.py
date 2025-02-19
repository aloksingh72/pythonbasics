# Dated:->19/02/2025/Wednesday

# Call by Value
# immutable objec: follow call by value(variable ki copy banegi)
# mutable: follow call by reference(extact variable jayega)
# A copy of the variable is passed, and modifications inside the function do not affect the original variable.


str = "Noida"
def update(str1):
    print(str1)
    str1 = "Delhi"
    print(str1)

print(str)
update(str)
print(str)


# Call by reference (mutable)
# When passing mutable objects (like list, dict, set), changes inside the function affect the original object because,
#  both the function parameter and the original reference point to the same memory location.

lst = [1,2,3]

def ref_update(lst1):
    print(lst1)
    lst1.append(4)
    print(lst1)
print(lst)
ref_update(lst)
print(lst)



# Shallow copy
# Deep copy


