class SalaryNotInRange(Exception):
    def __init__(self, salary):
        self.salary = salary
        self.msg = "Salary is not in range (5000, 30000)"
        
        super().__init__(self.msg)
        
sal = int(input("Enter salary :"))
if sal < 5000 or sal > 30000:
    raise SalaryNotInRange(sal)
else:
    print(sal)