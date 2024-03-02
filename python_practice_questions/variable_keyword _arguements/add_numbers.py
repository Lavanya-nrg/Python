# Define a function called 'adder' that takes variable number of arguments (*num)
def adder(*num):
    # Initialize a variable 'sum' to keep track of the total sum
    sum = 0
    
    # Iterate through each number in the provided arguments
    for n in num:
        # Add the current number to the total sum
        sum = sum + n
    
    # Print the total sum after processing all the arguments
    print("sum =", sum)

# Call the 'adder' function with a single argument 8
adder(8)

# Call the 'adder' function with two arguments 9 and 8
adder(9, 8)

# Call the 'adder' function with three arguments 2, 3, and 4
adder(2, 3, 4)
