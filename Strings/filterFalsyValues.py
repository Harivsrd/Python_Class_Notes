#Create a list of mixed data values remove falsy values from above list and create new list 

data = [0, "hello", 42, None, "world", False, "", 42]
#None --- remove all falsy values
res = list(filter(None, data))
print(res)