
# bute force: iterate over the linked list, store values in list, reverse it
# and create a new linkedlist with reveesed ele, return the new linkedlist

def reverseLinkedList(root):
    if not root:
        return None 
    prev = None 
    n = root
    while n is not None: 
        temp = n.ref
        n.ref = prev
        prev = n 
        n = temp

    return prev 

    