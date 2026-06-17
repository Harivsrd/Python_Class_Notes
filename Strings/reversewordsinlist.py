str = list(input("Enter list of strings: ").split()) 
print(str)
str = [x[::-1] for x in str] 
print(str)