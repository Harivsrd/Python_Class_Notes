def checkAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    d1 = {}
    for c in str1:
        if c not in str2:
            return False
        d1[c] = d1.get(c, 0) + 1
    d2 = {} 
    for c in str2:
        if c not in str1:
            return False 
        d2[c] = d2.get(c,0)+1 
        
    for k in d1.keys():
        if d1[k] != d1[k]:
            return False
    return True

str1 = input("Enter string1 :").lower()
str2 = input("Enter string2 :").lower()     

if(checkAnagram(str1, str2)):
    print(f"{str1} & {str2} are Anagrams")
else:
    print("Not anagrams")