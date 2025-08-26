
class lockableNode:
    def __init__(self, data , parent = None):
        self.data = data 
        self.parent = parent 
        self.children = []
        self.is_locked = False 
        self.locked_desc_count = 0

    def can_lock_or_unlock (self):
        if self.locked_desc_count > 0:
            return False 
        curr = self.parent
        while curr:
            if curr.is_locked:
                return False    
            curr = curr.parent 

        return True 

    def lock(self):
        if self.is_locked:
            return False 
        if not self.can_lock_or_unlock():
            return False 
        self.is_locked = True 
        curr = self.parent 
        while curr:
            curr.locked_desc_count += 1
            curr = curr.parent
        return True 

    def unlock(self):
        if not self.is_locked:
            return False 
        if not self.can_lock_or_unlock():
            return False 
        self.is_locked = False 
        curr = self.parent
        while curr:
            curr.locked_desc_count -= 1
            curr = curr.parent 
        return True

def preOrder(node):
    if not node:
        return  
    print(f"{node.data}", end = "->")
    for child in node.children:
        preOrder(child)

def details(node):
    if not node:
        return 
    print(f"node : {node.data}")
    print(f"children : {[child.data for child in node.children]}")
    print(f"parent : {node.parent}")
    print(f"=> => => =>")

root = lockableNode(1)
child2 = lockableNode(2, 1)
child3 = lockableNode(3, 1)
child2_1 = lockableNode(4, 2)
child2_2 = lockableNode(5, 2)
child2.children.extend([child2_1, child2_2])
root.children.extend([child2, child3])
details(root)
details(child2)
details(child3)
preOrder(root)









