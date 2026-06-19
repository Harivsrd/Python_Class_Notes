class Restaurant :
    def __init__(self):
        self.menu_list = []
        self.table_list = [1,2,3,4,5,6]
        self.reserved_tables = []
        self.orders = []
        
    def add_item(self, item):
        self.menu_list.append(item)
        
    def view_menu(self):
        print("Menu List :")
        for i, item in enumerate(self.menu_list):
            print(f"i.  {item[0]}  {item[1]} {item[2]}")
            
    def reserve_table(self):
        if len(self.table_list) == len(self.reserved_tables):
            print("All tables are reserved! Wait for some time")
            return
        for table in self.table_list:
            if table not in self.reserve_table:
                print("Table -",table)
        tno = int(input("Enter table no:"))
        self.reserved_tables.append(tno)
        print(f"Table - {tno} is reserved successfully!")
        return tno
        
    def order(self,customer_id,items):
        