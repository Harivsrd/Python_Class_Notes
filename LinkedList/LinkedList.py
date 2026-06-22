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