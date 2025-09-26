
from typing import Optional 

class TreeNode:
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.right , self.left = right, left 

class solution:
    def isSameTree(self, root1 : Optional[TreeNode], root2 : Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False 
            if p.val != q.val :
                return False 

            return helper(p.left, q.left) and helper(p.right, q.right)

        helper(root1, root2)
