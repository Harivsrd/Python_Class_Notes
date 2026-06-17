#Create a new String with 3 middle elements
str = input("Enter string :")

n = len(str) 
if n % 2 == 0:
    mid = n//2-1
else:
    mid = n//2 

newStr = str[mid-1] + str[mid] + str[mid+1]

print(newStr)