import LinkedList
values = list(map(int, input("Enter values to insert :").split()))

l = LinkedList.LinkedList()
for value in values :
    l.insert_end(value)
    
length = 0
curr = l.head
while curr :
    length += 1
    curr = curr.next

print("Length : ",length)