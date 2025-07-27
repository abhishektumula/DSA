from typing import List, LiteralString, Optional, ValuesView

class TreeNode:
    def __init__(self, val = None, left =None , right = None ):
        self.val = val 
        self.left = left 
        self.right = right 
        

class Solution:
    def array2BalancedTree (self, numbers : List[int]) -> Optional[TreeNode]:
        tabs = "    "
#        def inorderTraversal(root, prefix = "root : ", level = 0):
#            if root:
#                inorderTraversal(root.left,  "Left :", level+ 1)
#                print(f"{level * tabs} {prefix} {root.val}")
#                inorderTraversal(root.right,  "right :", level + 1)

        if not numbers:
            return None
        n = len(numbers)//2
        root = TreeNode(numbers[n])

        root.left = self.array2BalancedTree(numbers[:n])
        root.right = self.array2BalancedTree(numbers[n+1:])

        return root

s = Solution() 
print(s.array2BalancedTree([-10, -3, 0, 5, 9]))


