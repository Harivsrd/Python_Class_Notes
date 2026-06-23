import BST 

def print_leaf(nodes,root):
    if root:
        print_leaf(nodes,root.left)
        if not root.left and not root.right :
            nodes.append(root)
        print_leaf(nodes,root.right)
        
        
bst = BST.BST()
values = list(map(int, input("Enter values : ").split()))

for value in values :
    bst.root = bst.insert(bst.root,value)
    
print("Leaf values :")
nodes = []
print_leaf(nodes, bst.root)
print(len(nodes))
