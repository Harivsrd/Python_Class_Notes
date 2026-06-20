try:
    num1 = int(input())
    num2 = int(input())
    sum = num1 + num2 
    pro = num1 * num2 
    print(f"Sum : {sum}\nProduct : {pro}")
    quo = num1 / num2 
    print(f"Quotient : {quo}")
except ZeroDivisionError:
    print("Denominator should not be zero")
    print("Taken 2 as denominator as default!!!")
    quo = num1 / 2
    print(f"Quotient : {quo}")
