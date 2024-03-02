list_of_ints = [[1, 2, 3, 4], [2, 5, 6], [7, 8, 9, 10]]

def nested_ListComprehension():
   # let's prepare the nested list comprehension
   return [[x for x in inner_list if x%2 == 0] for inner_list in list_of_ints]

if __name__ == '__main__':

   evenNums = nested_ListComprehension()
   # print list of even numbers and its size
   print("Found {} list of even numbers: {}".format(len(evenNums), evenNums))