#NOTE: this file contains the implementation of the linked-list data structure 
#TODO: Insertion operations
#TODO: Traversal operations
#TODO: Deletion operations

import time
class node:
    def __init__(self, val:int):
        self.val = val
        self.ref = None
    def __str__(self):
       return str(self.val) 

class linkedlist:
    def __init__(self):
        self.head = None

    def InsertionAtEnd(self, value : int):
        if self.head is None:
            self.head = node(value)
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref 
            n.ref = node(value)

    def InsertionAtBegin(self, value : int):
        if not self.head:
            self.head = node(value)
        else:
            new_node = node(value)
            new_node.ref = self.head
            self.head = new_node

    def InsertionAfterTarget(self, target : int, value : int):
        if not self.head :
            print(f"linked list is empty...")
            return 
        n = self.head
        while n :
            if n.val == target:
                temp = n.ref 
                new_node = node(value)
                n.ref = new_node
                new_node.ref = temp 
                
            n = n.ref 
        
    def InsertionBeforeTarget(self, target : int, value : int):
        if not self.head:
            print(f"linked list is empty...")
            return 
        if self.head.val  == target:
            new_node = node(value)
            new_node.ref = self.head 
            self.head = new_node
        else:
            n = self.head
            while n:
                if n.ref.val == target:
                    temp = n.ref 
                    new_node = node(value)
                    n.ref = new_node
                    new_node.ref = temp 
                n = n.ref 
        return 

    def deleteNodeAtEnd(self):
        if not self.head :
            return f"linkedlist is empty...(deleteNodeAtEnd)"
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref 
            n.ref = None
    
    def deleteHeadNode(self):
        if not self.head:
            return f"linkedlist is empty...(deleteHeadNode)"
        else:
            self.head = self.head.ref 

    def deleteAfterNode(self, target : int) :
        if not self.head :
            return f"linked list is empty ...(delete aftere target node)"
        
        n = self.head
        while n.ref:
            if n.val == target:
                next = n.ref.ref
                n.ref = next 
                n = n.ref
            else:
                n = n.ref 

    def deleteBeforeNode(self, target : int):
        if not self.head :
            return f"linked-list is empty (delete before node...)"
        else:
            n = self.head 
            while n.ref :
                if n.ref.ref.val == target:
                    n.ref = n.ref.ref
                    n = n.ref 
                else:
                    n = n.ref 
        
    def Traversal(self):
        if not self.head:
            return "linked list is empty"
        n = self.head 
        while n:
            res = ""
            print(f"|{n.val}|-->", end ="", flush = True )
            res += str(n.val) + "-->"
            time.sleep(0.5)
            n = n.ref 

        return res


