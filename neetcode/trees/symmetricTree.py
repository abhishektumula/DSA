
from os import login_tty
from typing import Optional 

class TreeNode:
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.right , self.left = right, left 

class Solution:
    def isSymmetry(self, root : Optional[TreeNode]) -> bool:
        if not root:
            return False
        lPart , rPart = root.left, root.right
        def helper(p, q):
            if not p and not q:
                return True 
            if not p or not q:
                return False
            if p.val != q.val:
                return False 
            return helper(p.left, q.right) and helper(p.right, q.left)

        return helper(lPart, rPart)

