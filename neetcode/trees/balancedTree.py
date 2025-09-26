
from typing import Optional


class TreeNode:
    def __init__(self, val = 0, right = None, left = None) -> None:
        self.val = val
        self.left = left 
        self.right = right 

class Solution:
    def balancedTree(self, root : Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0 
            l_depth =  helper(node.left)
            r_depth =  helper(node.right)

            if abs(l_depth - r_depth) > 1 or l_depth == -1 or r_depth == -1:
                return -1
            
            return 1 + max(l_depth, r_depth)

        return helper(root) != -1

