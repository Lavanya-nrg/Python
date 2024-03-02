# Define a list 'elist' containing numbers from 1 to 99 (excluding 100)
elist = range(1, 100)

# Define a function 'list_comp' to filter even numbers from 'elist'
def list_comp():
    # Use list comprehension to create a new list 'elistnum' with even numbers from 'elist'
    elistnum = [x for x in elist if x % 2 == 0]
    
    # Return the list of even numbers
    return elistnum

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Call the 'list_comp' function and store the result in 'op'
    op = list_comp()
    
    # Print the count and the list of even numbers
    print("found {} even numbers: {}".format(len(op), op))
