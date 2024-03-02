# Write a program to remove characters from a string starting from zero up to n and return a new string.

def remn(words,n):
    print('original string:',words)
    x=words[n:]
    return x

print(remn('lavanya',4))