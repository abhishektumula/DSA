#NOTE: the problem statement defines to remove the value from the linked list
#NOTE: value may ocuur more than once -> iterate till the last node
#NOTE: remove the node , check the next node value in the current value
#NOTE: if the value is equal to target value, then remove the next reference from the present node
#NOTE: add the target nodes next value in the present/ previous node, the target is now unlinked 
#NOTE: itertare to the last node, where ref points to none..

def remove_target(head):
    if not head:
        return None 
    if not head.next and head.val == target:
        return None

    n = head
    while n and n.next:
        if n.next.val == target:
            temp = n.next.next
            n.next = temp 
        n= n.next

    return head 
