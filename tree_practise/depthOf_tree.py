from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):

        self.val = val
        self.left = left
        self.right = right


class Solution:

    def TreeDepth(self, treeStr : Optional[TreeNode]) -> int: 

        if not treeStr:
            return 0 
        
        l_depth = treeStr.left
        r_depth = treeStr.right 

        return 1 + max(self.TreeDepth(l_depth), self.TreeDepth(r_depth))
    
    

