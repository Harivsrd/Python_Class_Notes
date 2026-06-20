try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    
    res = a/b 
    print(res)
    
except ValueError:
    print("Inputs must be numeric!!")
    
except ZeroDivisionError:
    print("Denominator should not be zero")