# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers


def pal(num):
    onum=num
    revnum=0
    while num>0:
        rem=num%10
        revnum=(revnum*10)+rem
        num=num//10
        
    if onum==revnum:
        print('given number is palindrome')
    else:
        print('not a palindrome')


pal(121)
pal(89)