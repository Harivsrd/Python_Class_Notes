try:
    number = int(input("Enter input : "))
    print("Square :",number**2)
    print("Cube :",number**3)
except ValueError:
    print("Invalid input!")
    print("Give input as numeric only!!")
    