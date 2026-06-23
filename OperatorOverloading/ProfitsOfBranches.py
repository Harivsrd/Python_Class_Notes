class Branch:
    def __init__(self, name, profit):
        self.name = name
        self.profit = profit

    def __add__(self, other):
        return Branch("Merged", self.profit + other.profit)


b1 = Branch("Branch A", 50000)
b2 = Branch("Branch B", 75000)

merged = b1 + b2
print(merged)  
