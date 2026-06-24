import BST

def find_lca(root, n1,n2):
    if root is None:
        return None
    if n1 < root.data and n2 < root.data :
        return find_lca(root.left,n1,n2)
    if n1 > root.data and n2 > root.data:
        return find_lca(root.right,n1,n2)
    else:
        return root

bst = BST.BST()
values = list(map(int, input().split()))
for value in values:
    bst.root = bst.insert(bst.root, value)
bst.inorder(bst.root)

n1,n2 = map(int, input().split()) 

r = find_lca(bst.root,n1,n2)

print(r.data)
