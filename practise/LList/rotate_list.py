#NOTE: rotate linked list 

def rotate_linkedlist(ll, value : int) :
    dummy = ListNode()
    tail = dummy 
    if not head or not head.next:
        return head
    n = head
    arr = []
    while n:
        arr.append(n.val)
        n = n.next

    n = value % len(arr)
    for _ in range(n):
        arr.insert(0, arr.pop())
    
    for each in arr:
        tail.next = ListNode(each)
        tail = tail.next 

    return dummy.next
