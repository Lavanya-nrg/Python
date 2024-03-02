# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
def first_last(numlist):
    print('given list',numlist)
    firstnum=numlist[0]
    lastnum=numlist[-1]
    if firstnum==lastnum:
        return True
    else:
        return False
    
numberlist=[10,20,30,40,10]
print("result is",first_last(numberlist))