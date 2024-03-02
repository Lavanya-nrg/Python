def printingdata(name, *args, **kwargs):
    # Printing the main name
    print("I am", name)

    # Printing each argument in *args (a tuple)
    for arg in args:
        print("I am", arg)

    # Printing each key-value pair in **kwargs (a dictionary)
    for key, value in kwargs.items():
        print('I am', key, 'and my value is', value)

# Calling the function with positional argument '007', variable arguments 'agent',
# and keyword arguments firstname='john' and lastname='wood'
printingdata('007', 'agent', firstname='john', lastname='wood')
