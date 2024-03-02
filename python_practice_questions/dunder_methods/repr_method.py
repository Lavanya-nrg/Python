
class String:
    # Constructor to initialize the String object with a given string
    def __init__(self, string):
        self.string = string 

    # Representation method to return a string representation of the object
    def __repr__(self):
        return 'Object: {}'.format(self.string)

if __name__ == '__main__':
    # Creating an instance of the String class with the string 'Hello'
    string1 = String('Hello')

    # Printing the string representation of the String object
    print(string1)
