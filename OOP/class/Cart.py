class Cart:
    def __init__(self):
        self.items = {1:["TV", 12000],2:["Laptop",45000],3:["Fridge",78000]}
        self.cart = []
        
    def add_item(self,id):
        if id not in self.items:
            print("Item not available")
            return
        else:
            l = len(self.cart)+1
            self.cart.append((id,self.items[id]))
        
    def remove_item(self, id):
        for i,(item_id,item) in enumerate(self.cart):
            if item_id == id:
                self.cart.pop(i)
                return
        print("Item not in cart")
            
    def compute_total(self):
        total = 0
        for i,item in self.cart:
            total += item[1]
        return total
            
    def order(self):
        self.total = self.compute_total()
        print("Order details :")
        self.display_cart()
        print("Total :",self.total)
        
    def display_items(self):
        for k,v in self.items.items():
            print(f"{k} - {v[0]} - {v[1]}")
    
    def display_cart(self):
        if not self.cart:
            print("Cart is empty")
            return
        print("Cart Items :")
        print("\tId | Product | Price ")
        for item in self.cart:
            print('\t',item[0],'\t|', item[1][0],'\t|', item[1][1],'\t|')
        
        
cart = Cart() 
while True:
    print("--menu--")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display cart")
    print("4. Order")
    
    choice = int(input("Enter choice :"))
    if choice == 1:
        cart.display_items()
        id = int(input("Enter item id: "))
        cart.add_item(id)
    elif choice == 2:
        cart.display_cart()
        id = int(input("Enter id to remove :"))
        cart.remove_item(id)
    elif choice==3:
        cart.display_cart()
    elif choice==4:
        cart.order()
        break
    else:
        break
    