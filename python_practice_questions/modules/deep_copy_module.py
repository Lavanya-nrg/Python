# Write a Python program to create a deep copy of a given dictionary. Use copy.copy

import copy

# First set of operations

# Creating a dictionary
nums_x = {"a": 1, "b": 2, 'cc': {"c": 3}}

# Displaying the original dictionary
print("Original dictionary: ", nums_x)

# Creating a deep copy of the dictionary
nums_y = copy.deepcopy(nums_x)
print("\nDeep copy of the said list:")
print(nums_y)

# Changing the value of an element in the original dictionary
nums_x["cc"]["c"] = 10
print("\nUpdated original dictionary:")
print(nums_x)

# Displaying the second dictionary (Deep copy)
print("\nSecond dictionary (Deep copy):")
print(nums_y)


# Second set of operations

# Creating another dictionary
nums = {"x": 1, "y": 2, 'zz': {"z": 3}}

# Displaying the original dictionary
print("\nOriginal dictionary :")
print(nums)

# Creating a deep copy of the dictionary
nums_copy = copy.deepcopy(nums)
print("\nDeep copy of the said list:")
print(nums_copy)

# Changing the value of an element in the original dictionary
nums["zz"]["z"] = 10
print("\nUpdated original dictionary:")
print(nums)

# Displaying the second dictionary (Deep copy)
print("\nSecond dictionary (Deep copy):")
print(nums_copy)
