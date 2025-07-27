from  random import randint
from typing import Optional

from utility import uniqueList


class TreeNode:
    
    def __init__(self, val = 0, left = None, right = None ):
        self.val = val 
        self.left = left 
        self.right = right 


    def insertion(self, root , target : int):

        if target > root.val:
            if root.right:
                return self.insertion(root.right, target)
            else:
                root.right = TreeNode(target)

        elif target < root.val:
            if root.left:
                return self.insertion(root.left, target)
            else:
                root.left = TreeNode(target)

        else:
            return 

        return root


tabs = "    "

def inorderTraversal (node, prefix = "Ro --> ", level = 0):
    if node:
        inorderTraversal(node=node.right, prefix="R -->", level=level+1)
        print(f"{tabs * level} {prefix} {node.val}")
        inorderTraversal(node=node.left, prefix="L -->", level=level+1)

ele = uniqueList(10, [1, 15])
root = TreeNode(ele[0])
for i in range(1, len(ele)):
    root.insertion(root, ele[i])

inorderTraversal(root)


