class rect:
    def __init__(self, *args, **kwargs):
        # Unpack args to get length and width
        self.length, self.width = args

        # Set default values for color and label using kwargs
        self.color = kwargs.get('color', 'white')  # Default color is 'white' if not provided
        self.label = kwargs.get('label', None)     # Default label is None if not provided

# Create instances of the rect class with different parameters
rect1 = rect(4, 5, color='blue', label='rectangle a')
rect2 = rect(2, 7, color='red')

# Access and print the attributes of the rect instances
print(rect1.color)  # Output: blue
print(rect2.label)  # Output: None
