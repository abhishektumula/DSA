from typing import Optional
class TreeNode:

    def __init__(self, val = 0, left = None, right = None ):
        self.val = val 
        self.left = left 
        self.right = right 



class Solution:
    def minimumDepth(self, treeStr : Optional[TreeNode]) -> int:

        if not treeStr:
            return 0 
        
        if not treeStr.left:
            return self.minimumDepth(treeStr.right)

        if not treeStr.right:
            return self.minimumDepth(treeStr.left)

        return 1 + min(self.minimumDepth(treeStr.left), self.minimumDepth(treeStr.right))



