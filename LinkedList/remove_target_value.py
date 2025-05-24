import time
class node:
    def __init__(self, data):
        self.data = data
        self.ref = None 

class linkedlist:
    def __init__ (self):
        self.head = None

    def insert(self,value):
        if not self.head :
            self.head = node(value)
        else:
            n = self.head
            while n.ref:
                n = n.ref 
            newnode = node(value)
            n.ref = newnode

    def traversal(self):
        if not self.head:
            return f"techincally returns None, for debuggin it return LL is empty, .. don't worry"
        n = self.head
        while n:
            print(f"{n.data}-->",end ="", flush = True)
            time.sleep(0.4)
            n = n.ref
    def removeTarget(self, target : int):
        if not self.head:
            return f"head is none.."
        if self.head.ref is None and self.head.data == target:
            self.head = None
            return self.head
        n = self.head
        while n and n.ref :
            if n.ref.data == target:
                n.ref = n.ref.ref 
            else:
                n = n.ref 

ll = linkedlist()
numbers = [6]
for i in numbers:
    ll.insert(i)
print(ll.traversal())
ll.removeTarget(6)
print(ll.traversal())
