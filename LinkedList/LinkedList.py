class Node :
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert_head(self, x):
        t = Node(x)
        t.next = self.head
        self.head = t
        return self.head 
    
    def insert_end(self, x):
        t = Node(x)
        if not self.head:
            self.head = t 
        else :
            curr = self.head 
            while curr.next :
                curr = curr.next 
            curr.next =  t 
        return self.head
    
    def insert_middle(self, x, pos):
        if pos < 1:
            return self.head 
        t = Node(x) 
        if pos == 1:
            t.next = self.head 
            self.head = t
        else :
            curr = self.head 
            for i in range(1,pos-1):
                if curr == None :
                    return self.head 
                curr = curr.next 
            if curr == None :
                return self.head
            t.next = curr.next
            curr.next = t 
        return self.head 
    
    def delete_head(self):
        if self.head is None:
            return self.head 
        else:
            t = self.head 
            self.head = self.head.next 
            t = None 
        return self.head 
    
    def delete_end(self):
        if self.head is None:
            return self.head 
        if self.head.next is None:
            self.head = None
        else:
            curr = self.head 
            while curr.next:
                prev = curr 
                curr = curr.next 
            prev.next = None 
            curr = None 
        return self.head 
    
    def delete_pos(self,pos):
        t = self.head 
        if self.head==None or pos < 1:
            return self.head 
        if pos == 1 :
            self.head = self.head.next 
            t.next = None  
        else:
            prev = None 
            curr = self.head 
            for i in range(1,pos):
                prev = curr 
                curr = curr.next 
            prev.next = curr.next 
            curr.next = None 
        return self.head 
    
    def traversal(self):
        curr = self.head 
        while curr :
            print(curr.data,end='->')
            curr = curr.next 
        
    def search(self,x):
        curr = self.head 
        while curr :
            if curr.data == x:
                return True
            curr = curr.data  
        return False 

l = LinkedList()
        
while True:
    print("\n Menu ---")
    print("1. Insert at head")        
    print("2. Insert at end")        
    print("3. Insert at pos")        
    print("4. delete at head")        
    print("5. delete at end")        
    print("6. delete at pos")  
    print("7. Traversal") 
    print("8.Search") 
    print("9.exit")   
    
    choice = int(input("Enter choice: "))
    if choice == 1:
        x = int(input("Enter value :"))
        l.head = l.insert_head(x)
    elif choice == 2:
        x = int(input("Enter value :"))
        l.head = l.insert_end(x)
    elif choice == 3:
        x = int(input("Enter value :"))
        pos = int(input("Enter pos :"))
        l.head = l.insert_middle(x,pos)
    elif choice == 4:
        l.head = l.delete_head()
    elif choice == 5:
        l.head = l.delete_end()
    elif choice == 6:
        pos = int(input("Enter pos :"))
        l.head = l.delete_pos(pos)
    elif choice == 7:
        l.traversal()
    elif choice == 8:
        x = int(input("Enter search ele :"))
        res = l.search(x)
        if res:
            print("Found")
        else:
            print("Not found")
    else:
        break
            