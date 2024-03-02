# Function definition: makesentence takes variable keyword arguments (**words)
def makesentence(**words):
    # Initialize an empty string to store the sentence
    sentence = ''
    
    # Iterate through the values of the keyword arguments
    for word in words.values():
        # Concatenate each word to the sentence
        sentence += word
    
    # Return the final sentence
    return sentence

# Example usage of makesentence function
print("sentence:", makesentence(a="lavanya", b="narang", c="is", d="a", e="girl"))
