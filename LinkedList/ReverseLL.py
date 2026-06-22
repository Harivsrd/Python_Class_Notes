import LinkedList

def reverse_linkedlist(root):
    prev = None 
    curr = root 
    
    while curr:
        nxt = curr.next
        curr.next = prev 
        prev = curr 
        curr = nxt 
    
    return prev

    

l = LinkedList.LinkedList() 

n = int(input("Enter no of elements :"))
values = list(map(int, input().split()))

for value in values:
    l.insert_end(value)

l.head = reverse_linkedlist(l.head)

print("Linked list :",end=" ")   
l.traversal()
