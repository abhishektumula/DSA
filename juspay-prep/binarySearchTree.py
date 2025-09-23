
from collections import deque
import random
from typing import List

class bTree:
    def __init__(self, val =0 , left = None, right = None) -> None:
        self.val = val
        self.left = left 
        self.right = right 
        pass

    def addtoTree (self, root, target : int):
        if not root:
            root = bTree(val=target)
            return root
        if target == root.val:
            return root 
        elif target > root.val:
            if root.right:
                self.addtoTree(root.right, target)
                return root 
            else:
                root.right = bTree(val=target)
                return root 
        else:
            if root.left:
                self.addtoTree(root.left, target)
                return root
            else:
                root.left= bTree(val=target)
                return root 

def levelOrder(root) -> List:
    if not root:
        return [] 
    result = [] 
    quq = deque([root])
    while quq:
        length = len(quq)
        inner = [] 
        for _ in range(length):
            node = quq.popleft()
            inner.append(node.val)
            if node.left:
                quq.append(node.left)
            if node.right:
                quq.append(node.right)

        result.append(inner)
    
    return result

def levelOrder2(root) -> List:
    if not root:
        return [] 
    result = [] 
    quq = deque([root])
    while quq:
        length = len(quq)
        inner = [] 
        for _ in range(length):
            node = quq.popleft()
            if node:
                inner.append(node.val)
                quq.append(node.left)
                quq.append(node.right)
            else:
                inner.append(-1)
                quq.append(None)
                quq.append(None)

        if all(i == -1 for i in inner):
            break
        result.append(inner)
    
    return result
ele = [random.randint(1, 10) for _ in range(100)]
root = bTree(ele[0])
for i in range(1, len(ele)):
    root = root.addtoTree(root, ele[i])
ans = (levelOrder2(root))
for i in ans:
    print(i)









