class String:
    def __init__(self, string):
        self.string = string

    # Define the __str__ method to customize the string representation
    def __str__(self):
        return self.string

if __name__ == '__main__':
    string1 = String('Hello')
    # Now, when you print the object, it will display the actual string content
    print(string1)
