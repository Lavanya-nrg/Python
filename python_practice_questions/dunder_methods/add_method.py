
class String: 
    def __init__(self, string): 
        self.string = string 
        
    def __repr__(self): 
        return 'Object: {}'.format(self.string) 
    
    def __add__(self, other): 
        return self.string + other 

if __name__ == '__main__':
    # Create an instance of the String class with the initial string 'Hello'
    string1 = String('Hello') 

    # Concatenate ' Geeks' to the string using the __add__ method
    print(string1 +' Geeks') 
