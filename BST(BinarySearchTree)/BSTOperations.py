import BST

bst = BST.BST()

while True:
    print("\n ---menu---")
    print("1. Insert (recursion)")
    print("2. Insert (iteration)")
    print("3. Delete (recursion)")
    print("4. Delete (iteration)")
    print("5. BST Traversal :")
    
    choice = int(input("Enter choice :"))
    
    if choice == 1:
        x = int(input("Enter data :"))
        bst.root = bst.insert(bst.root,x)
    elif choice == 2:
        x = int(input("Enter data :"))
        bst.root = bst.insert1(x)
    elif choice == 3:
        x = int(input("Enter ele :"))
        bst.root = bst.delete(bst.root,x)
    elif choice == 4:
        x = int(input("Enter ele :"))
        bst.root = bst.delete1(x)
    elif choice == 5 :
        print("1. Inorder Traversal")
        print("2. Preorder Traversal")
        print("3. Postorder Traversal")
        ch = int(input("Enter choice :"))
        if ch == 1:
            bst.inorder(bst.root)
        elif ch==2:
            bst.preorder(bst.root)
        elif ch==3:
            bst.postorder(bst.root)
        else:
            continue
            
    else:
        break