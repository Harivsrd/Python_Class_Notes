from functools import reduce


li = [1, 2, 3, 4, 5]
tot = reduce(lambda x,y: x+y, li)
print(tot)