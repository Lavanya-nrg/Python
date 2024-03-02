# Write a program to count the total number of digits in a number using a while loop.
num=34567
cnt=0
while num!=0:
    num=num//10
    cnt=cnt+1

print('total digits are:',cnt)