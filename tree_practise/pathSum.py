from typing import Optional


class TreeNode:
    def __init__(self, val =0, left = None, right = None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 


class Solution:
    def hasPathSum (self, treeStr : Optional[TreeNode], target : int) -> bool:

        def fn(node, currentSum) : 
            if not node:
                return False

            currentSum += node.val 

            if not node.left and not node.right:
                return currentSum == target 

            return fn(node.left, currentSum) or fn(node.right, currentSum) 

        return fn(treeStr, 0)

        

