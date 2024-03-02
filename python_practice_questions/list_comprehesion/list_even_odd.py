#Make a single list comprehension to return two lists, one for even and another for odd numbers.

even=range(1,100)
onum=[]
enum=[]

def list_comp():
    return [x for x in even if x%2==0 or onum.append(x)]

if __name__ == '__main__':

   enum = list_comp()
   # print list of even numbers and its size
   print("Found {} even numbers: {}".format(len(enum), enum))
   # print list of odd numbers and its size
   print("Found {} odd numbers: {}".format(len(onum), onum))