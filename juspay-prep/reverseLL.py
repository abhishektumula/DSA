import random
class Node:
    def __init__(self, val = 0, ref = None):
        self.val = val 
        self.ref = ref 

class linkedList:
    def __init__(self) -> None:
        self.head = None
        pass

    def insertion(self, target : int) :
        if not self.head:
            self.head = Node(target)
            return 
        n = self.head 
        while n.ref :
            n = n.ref 
        n.ref = Node(target)

    def display(self, head = None):
        if not head:
            return 
        n = head 
        while n:
            print(f"{n.val}", end = "->")
            n = n.ref 

        print("\n")

    def reversell(self,head):
        if not head:
            return 
        curr = head 
        prev = None 
        while curr:
            nxt = curr.ref 
            curr.ref = prev 
            prev = curr
            curr = nxt 

        return prev 

ll = linkedList()
ele = [random.randint(1,10) for _ in range(10)]
for each in ele:
    ll.insertion(each)

ll.display(ll.head)
ans = ll.reversell(ll.head)
ll.display(ans)









