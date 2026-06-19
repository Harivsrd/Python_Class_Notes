import re

text = "Hari's email is hari123@example.com and phone is 9876543210"

email = re.findall(r'\b[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print("Email:", email)

phone = re.findall(r'\d{10}', text)
print("Phone:", phone)

masked = re.sub(r'\d', 'X', text)
print("Masked:", masked)
