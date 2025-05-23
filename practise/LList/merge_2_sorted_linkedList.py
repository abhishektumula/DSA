#TODO: iterarate throught both linkedlists sametime 
#TODO: compare values, insert the least value to the res list
#TODO: change the list1/list2 pointer and also the res pointer 

#NOTE: change the both pointers....
from operations import *
def merge_linkedlist(list1, list2):
    head = node()
    dummy = head 
    n, m = list1, list2
    while n and m :
        if n.val <= m.val:
           dummy.next = node(n.val)
            n = n.next 
            dummy = dummy.next 
        else:
            dummy.next = node(m.val)
            m = m.next 
            dummy = dummy.next 

    while n:
        dummy.next = node()
        n = n.next 
        dummy = dummy.next 

    while m:
        dummy.next = node()
        m = m.next 
        dummy = dummy.next 

    return head.next 

ll = linkedlists()
a = [1,2,3,4,5,6]
for i in a:
    ll.insert(i)

print(ll.Traversal())

