words = list(input().split())

dict = {}

for word in words:
    key = "".join(sorted(word))
    if key in dict:
        dict[key].append(word)
    else:
        dict[key] = [word]
        
for k,v in dict.items():
    print(v)