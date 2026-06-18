class Book :
    def __init__(self,title, author, publisher, price):
        self.__title = title 
        self.__author = author 
        self.__publilsher = publisher 
        self.__price = price
        
        
    def computeDiscount(self, noc):
        if noc > 400 :
            return 50
        elif noc > 300:
            return 40
        elif noc > 200:
            return 20 
        elif noc > 100:
            return 10
        else:
            return "No Discount"
        
    def purchase(self,noc):
        self.__noc = noc
        self.total = self.__noc * self.__price
        self.discount = self.computeDiscount(self.__noc)
        self.total -= self.total * (self.discount/100)
        
    def display(self):
        print("------Purchase of Books Details-------")
        #print("| BookName | Author | Price | Noc | Discount | Total |")
        #print(f"{self.__title}\t|{self.__author}\t|{self.__price}\t|{self.__noc}\t|{self.discount}% \t|{self.total}")
        print("Title: ",self.__title)
        print("Author :",self.__author)
        print("Price :", self.__price)
        print("No of copies :", self.__noc)
        print("Discount :", self.discount,"%")
        print("Total :", self.total)
        
title = input("Enter title :")
author = input("Enter Author :")
publisher = input("Enter Publisher :")
price = int(input("Enter price :"))
noc = int(input("Enter no of copies: "))
b = Book(title, author, publisher, price)
b.purchase(noc)
b.display()
