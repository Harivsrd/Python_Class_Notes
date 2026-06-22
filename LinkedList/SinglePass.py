import LinkedList

def single_pass_method(root):
    slow , fast = root, root
    while fast and fast.next :
        slow = slow.next 
        fast = fast.next.next 
        
    return slow.data

l = LinkedList.LinkedList() 

n = int(input("Enter no of elements :"))
values = list(map(int, input().split()))

for value in values:
    l.insert_end(value)

l.traversal()  
  
res = single_pass_method(l.head)  
print("\n",res)
