str = input("Enter string :")

# li = []
# for i in range(0,len(str)):
#     r = i
#     word = ""
#     while r < len(str):
#         word = word + str[r]
#         if len(word) > 1 and word == word[::-1]:
#             li.append(word)
#         r+=1
        
# print(li)

li = []
l = 0
r = 0
word = ''
while r < len(str):
    word = word + str[r]
    if len(word) > 1 and word == word[::-1]:
        li.append(word)
    r += 1
l+=1
while l < len(str):
    word = str[l:r]
    if len(word)> 1 and word == word[::-1]:
        li.append(word)
    l+=1
    
print(li)
    

li = []
    
    