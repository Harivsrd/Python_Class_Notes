class InvalidAgeException(Exception):
    pass 

try:
    age = int(input("Enter age :"))
    if age < 18:
        raise InvalidAgeException
    else:
        print("Eligible")
except InvalidAgeException:
    print("Not eligible")