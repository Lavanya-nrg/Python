# Given two integer numbers, return their product only if 
#the product is equal to or lower than 1000. Otherwise, return their sum

def prod_or_sum(n1,n2):
        prod=n1*n2
        if prod<=1000:
                return prod
        else:
            return n1+n2
        
res=prod_or_sum(20,30)

print("result=",res)

result=prod_or_sum(40,30)

print("result",result)