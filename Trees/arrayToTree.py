import random
from typing import Optional
from typing import List

class TreeNode:

    def __init__(self, val = 0, left = None , right = None):
        self.val = val 
        self.left = left 
        self.right = right 

    def __str__(self) -> str:
        return f"treenode is created with {self.val} parameter"

    
    def insertNode (self, root , node : int ):
        if not root:
            root = TreeNode(node)

        if root.val < node:
            if self.right:
                return self.insertNode(root.right, node)
            else:
                root.right = TreeNode(node)

        elif root.val > node:
            if root.left:
                return self.insertNode(root.left, node)
            else:
                root.left = TreeNode(node)
        else:
            pass 

        return root
    
class Solution:

    def __str__(self) -> str:
        return f"class Solution is called."

    def arrayToTree(self, numbers : List ) -> Optional[TreeNode]:
        if not numbers:
            return None 

        root = TreeNode(numbers[0]) 
        for i in range(1, len(numbers)):
            root.insertNode(root, numbers[i])
        
        tabs = "    "
        def inorderTraversal (node, level = 0, prefix = "root:"):
            if node:
                inorderTraversal(node.left)
                print(f"{node.val}", end =" --")
                inorderTraversal(node.right)
#                inorderTraversal(node.left, level+1, "left:")
#                print(f"{tabs * level} {prefix} {node.val}")
#                inorderTraversal(node.right, level+1, "right:")


        inorderTraversal(root)
        
eles = random.sample(range(-20, 21), 15) 
cs = Solution()
print(cs)
print(cs.arrayToTree(eles))

