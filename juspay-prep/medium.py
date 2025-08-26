import time as time 
from typing import List, Optional
class Node:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val 
        self.next = next 
class LinkedList:    
    def make(self, value : int, head : Node):
        if head is None:
            newNode = Node(value)
            head = newNode
        else:
            n = head 
            while n.next is not None:
                n = n.next  
            n.next = Node(value)

        return head 

    def display(self, head):
        if not head:
            return -1 
        n = head 
        while n is not None:
            print(f"{n.val} ->", end = " ")
            time.sleep(0.5)
            n = n.next

class Solution:
    def mergeNode(self, nodes : Optional[Node]) -> Optional[Node]:
        if not nodes:
            return None 
        
        asd = Node()
        dummy = asd
        cur, curSum  = nodes.next, 0 
        while cur is not None:
            if cur.val == 0:
                dummy.next = Node(curSum)
                dummy = dummy.next 
                curSum = 0
            else:
                curSum += cur.val 
            cur = cur.next 

        return asd

nodeclass = LinkedList() 

eles = [0,1,0,3,0,2,2,0]
head = Node(eles[0])
for each in eles[1:]:
    head = nodeclass.make(each, head=head )

print(nodeclass.display(head=head))
cl = Solution()
ans = cl.mergeNode(nodes= head)
nodeclass.display(head=ans)
for i in range(10):
    print(f"\r countdown : {i}", end = "", flush=True)
print(f'end')
