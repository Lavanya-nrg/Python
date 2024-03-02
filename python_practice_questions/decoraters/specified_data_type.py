# Write a Python program to create a decorator to convert the return value of a function to a specified data type. 
# Define a decorator factory function that takes a data type as an argument
def convert_to_data_type(data_type):
    # Define the actual decorator that takes a function as an argument
    def decorator(func):
        # Define the wrapper function that applies the conversion to the result of the original function
        def wrapper(*args, **kwargs):
            # Call the original function and store the result
            result = func(*args, **kwargs)
            # Convert the result to the specified data type
            return data_type(result)
        # Return the wrapper function
        return wrapper
    # Return the decorator function
    return decorator

# Apply the @convert_to_data_type(int) decorator to the add_numbers function
@convert_to_data_type(int)
def add_numbers(x, y):
    return x + y

# Call the decorated add_numbers function and print the result and its type
result = add_numbers(10, 20)
print("Result:", result, type(result))

# Apply the @convert_to_data_type(str) decorator to the concatenate_strings function
@convert_to_data_type(str)
def concatenate_strings(x, y):
    return x + y

# Call the decorated concatenate_strings function and print the result and its type
result = concatenate_strings("Python", " Decorator")
print("Result:", result, type(result))

