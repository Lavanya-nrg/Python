# The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

num1,num2=0,1
print('fibonnaci series')
for i in range(10):
    print(num1,end=" ")
    res=num1+num2
    num1=num2
    num2=res
