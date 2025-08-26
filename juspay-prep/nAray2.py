
class Node:
    def __init__(self, data, parent = None) -> None:
        self.data = data
        self.parent = parent 
        self.children = []
        self.is_locked = False 
        self.locked_desc_count = 0
        pass

    def isLockable_UnLockable(self):
        if self.locked_desc_count > 0:
            return False 
        if self.is_locked:
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
        if not self.isLockable_UnLockable():
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
        if not self.isLockable_UnLockable():
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
    print(f"{node.data}", end="=>")
    for chidl in node.children:
        preOrder(chidl)


def details(node):
    if not node:
        return False 
    print(f"node value => {node.data}")
    print(f"children -> {[child.data for child in node.children]}")
    print(f"node parent => {node.parent}")

root = Node(1)                       
child2 = Node(2, 1)                  
child3 = Node(3, 1)                  
child2_1 = Node(4, 2)                
child2_2 = Node(5, 2)                
child2.children.extend([child2_1, child2_2]) 
root.children.extend([child2, child3])       
details(root)                                
details(child2)                              
details(child3)                              
preOrder(root)                               









