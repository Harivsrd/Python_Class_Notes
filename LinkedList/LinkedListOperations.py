import LinkedList
l = LinkedList.LinkedList()
        
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
            