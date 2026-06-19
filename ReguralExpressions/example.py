import re
text = input()
l = re.findall(r"\b[aA]\w*", text)
print(l)

l1 = re.findall(r"\br\w*o\b", text)
print(l1)

l2 = re.findall(r"\d+", text)
print(l2)

l3 = re.findall(r"\b[gG]\w*\b|\b\w*[gG]\b", text)
print(l3)

l4=re.sub(r"\d+", "###", text)
print(l4)

l5 = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.fullmatch(l5,text):
    print("Valid Email")
else:
    print("Invalid Email")