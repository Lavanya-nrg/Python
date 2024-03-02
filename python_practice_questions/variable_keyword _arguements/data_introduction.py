# Define a function 'intro' that accepts keyword arguments using **data
def intro(**data):
    # Print the type of the data parameter
    print("type of data: ", type(data))

    # Iterate through the key-value pairs in the 'data' dictionary
    for key, value in data.items():
        # Print the key and value in a formatted string
        print("{} is {}".format(key, value))

# Example 1: Calling the 'intro' function with 'firstname', 'lastname', 'age', and 'phonenumber'
intro(firstname="lavanya", lastname="narang", age=22, phonenumber=98877655)

# Example 2: Calling the 'intro' function with 'firstname', 'lastname', 'age', 'email', and 'country'
intro(firstname="lavanya", lastname="narang", age=22, email="john@gmail.com", country="india")

