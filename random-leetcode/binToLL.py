
from typing import NoReturn


class Node:
    def __init__(self, val = '', ref = None ) -> None:
        self.val = val 
        self.ref = ref
        pass

class LinkedList:
    def __init__(self) -> None:
        self.head = None 
        pass

    def insertion(self, target) -> None:
        if not self.head:
            newNode = Node(target)
            self.head = newNode
            return 
        n = self.head 
        while n.ref:
            n = n.ref 

        newNode = Node(target)
        n.ref = newNode
        return 

    def display(self) -> None :
        if not self.head:
            return 
        n = self.head 
        while n:
            print(f"{n.val}", end = '=>')
            n = n.ref 

        print("\n")
        return 


ll = LinkedList()
ele = [list(bin(i)[2:]) for i in range(1, 11) ]
#print(ele)

for ch in ele:
    ll = LinkedList()
    for i in ch:
        ll.insertion(i)
    ll.display()









