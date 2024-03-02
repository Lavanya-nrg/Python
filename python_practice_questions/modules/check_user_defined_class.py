# Write a Python program to check if a given value is a method of a
# user-defined class. Use types.MethodType()

# Importing the 'types' module to work with types in Python
import types

# Defining a class C
class C:
    # Method x of class C
    def x():
        return 1
    
    # Method y of class C
    def y():
        return 1    

# Function b
def b():
    return 2

# Checking if C().x is an instance of types.MethodType
print(isinstance(C().x, types.MethodType))

# Checking if C().y is an instance of types.MethodType
print(isinstance(C().y, types.MethodType))

# Checking if b is an instance of types.MethodType
print(isinstance(b, types.MethodType))

# Checking if max is an instance of types.MethodType (Note: max is a built-in function)
print(isinstance(max, types.MethodType))

# Checking if abs is an instance of types.MethodType (Note: abs is a built-in function)
print(isinstance(abs, types.MethodType))
