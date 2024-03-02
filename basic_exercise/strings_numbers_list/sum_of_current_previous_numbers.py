# Print the sum of the current number and the previous number

prev=0
print("Printing current and previous number sum in a range(10)")
for i in range(0,11):
    sum=prev+i
    print("Current number ",i," Previous number ", prev,"Sum: ",sum)
    prev=i