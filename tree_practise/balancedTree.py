from typing import Optional



class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution:
    def isBalanced (self, treeStr : Optional[TreeNode]) -> bool:
        if not treeStr: return True
        def checkDepth (root):
            node = root
            if not node:
                return 0 

            lef = checkDepth(node.left)
            rig = checkDepth(node.right)
            
            if lef == -1 or rig == -1 or abs(lef - rig) > 1:
                return -1 

            return 1 + max(lef, rig)


        return checkDepth(treeStr)!= 1


