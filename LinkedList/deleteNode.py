#NOTE:  just delete the node,
#NOTE: change the reference
#NOTE: simple stuff
#NOTE: 
#NOTE: 


def deleteNode(head, target: int ) :
    if not head :
        return head
    if head.ref is None and head.val == target:
        return None
    n = head
    while n and n.ref:
        if n.ref.val == target:
            n.ref = n.ref.ref 

    return n
