import LinkedList

def two_pass_method(root):
    curr = root 
    l = 0
    while curr :
        l+=1 
        curr = curr.next 
        
    print("length ",l)
    curr = root
    mid = l // 2 if l % 2 != 0 else l // 2 -1
    for i in range(mid):
        curr = curr.next 
        
    return curr.data 

l = LinkedList.LinkedList() 

n = int(input("Enter no of elements :"))
values = list(map(int, input().split()))

for value in values:
    l.insert_end(value)

l.traversal()  
  
res = two_pass_method(l.head)  
print(res)
