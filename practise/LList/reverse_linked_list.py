#TODO: write method to insert all the elements to the linked-list
#TODO: write another function to reverse the linked-list
#TODO: return the reversed linked-list

from operations import node, linkedlist 

def reverse_linkedlist(numbers):
    if not numbers.head:
        return numbers
    prev = None 
    n = numbers.head 
    while n:
        temp = n.ref 
        n.ref = prev
        prev = n 
        n = temp 
    numbers.head = prev
    return numbers

a = [1,2,3,4,5,6]
ll = linkedlist()
for each in a:
    ll.InsertionAtEnd(each)

print(ll.Traversal())
print(reverse_linkedlist(ll))


 
