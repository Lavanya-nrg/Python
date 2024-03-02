# Print characters from a string that are present at an even index number
word=input("enter word")
print("original string:",word)
size=len(word)
for i in range(0,size,2):
    print(word[i])