import BST 

def print_leaf(root):
    if root:
        print_leaf(root.left)
        if not root.left and not root.right :
            print(root.data,end=" ")
        print_leaf(root.right)
        
        
bst = BST.BST()
values = list(map(int, input("Enter values : ").split()))

for value in values :
    bst.root = bst.insert(bst.root,value)
    
print("Leaf values :")
print_leaf(bst.root)
