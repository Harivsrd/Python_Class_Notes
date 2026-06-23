class Node :
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, x):
        if root is None:
            return Node(x)
        if x < root.data:
            root.left = self.insert(root.left, x)
        elif x > root.data:
            root.right = self.insert(root.right, x)
        else:
            print("Duplicate")
            return root
        return root
    
    def insert1(self, x):
        t = Node(x)
        if self.root is None:
            self.root = t
            return
        curr = self.root
        par = None
        while curr:
            par = curr
            if x < curr.data:
                curr = curr.left
            elif x > curr.data:
                curr = curr.right
            else:
                print("Duplicate")
                return
        if x < par.data:
            par.left = t
        else:
            par.right = t
    
    def delete(self, root, x):
        if root is None:
            return None
        
        if x < root.data:
            root.left = self.delete(root.left, x)
        elif x > root.data:
            root.right = self.delete(root.right, x)
        else:
            if root.left is None and root.right is None:
                return None
            
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            succ = self.find_min(root.right)
            root.data = succ.data
            root.right = self.delete(root.right, succ.data)
        
        return root
    
    def delete1(self, x):
        curr = self.root
        par = None
        
        while curr and curr.data != x:
            par = curr
            if x < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        
        if curr is None:
            print("Not found")
            return
        
        if curr.left is None and curr.right is None:
            if par is None: 
                self.root = None
            elif par.left == curr:
                par.left = None
            else:
                par.right = None
        
        elif curr.left is None or curr.right is None:
            child = curr.left if curr.left else curr.right
            if par is None:
                self.root = child
            elif par.left == curr:
                par.left = child
            else:
                par.right = child
        
        else:
            succ_par = curr
            succ = curr.right
            while succ.left:
                succ_par = succ
                succ = succ.left
            
            curr.data = succ.data
            
            if succ_par.left == succ:
                succ_par.left = succ.right
            else:
                succ_par.right = succ.right

    
    def find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

            
        
        