str = input("Enter String: ")
n = len(str)
if n % 2 == 0:
    idx = n//2 -1 
else:
    idx = n//2
newStr = str[0] + str[idx] + str[n-1]
print(newStr)