#NOTE: create a array to add elements of one list (headA), arr = [contains all values of headA]
#NOTE: Now iterate thoorught the headB and check each value of node is present in the arr values
#NOTE: if any value present then return the remainig likedllist if wanted or return thr value and breka out of loop
#NOTE: don't do over engineering  
#NOTE: if it works, never touch it again...

def insertion_detection(headA , headB) :
    elements = []
    if not headA:
        return headB
    if not headB:
        return headA
    n = headA
    while n:
        elements.append(n.val)
        n = n.next 

    m = headB
    while m:
        if m.val in elements:
            return m 
        m = m.next
