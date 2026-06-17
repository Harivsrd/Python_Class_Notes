from functools import reduce 

li = [1, 2, 3, 4, 5]

max1 = reduce(lambda x,y: x if x > y else y, li)

print("Max :",max1)