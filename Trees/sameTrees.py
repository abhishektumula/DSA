from typing import Optional

class TreeNode:

    def __init__(self, val = 0, left = None, right = None ):
        self.val = val 
        self.left = left
        self.right = right 


class Solution:

    def isSameTree (self, tree1 :Optional[TreeNode], tree2 : Optional[TreeNode]):
        if not tree1 and not tree2:
            return True 

        if not tree1 or not tree2:
            return False 


        if tree1.val != tree2.val:
            return False 


        return self.isSameTree(tree1.left, tree2.left) and self.isSameTree(tree1.right, tree2.right)


