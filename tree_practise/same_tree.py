from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None , right = None):
        self.val = val 
        self.left = left
        self.right = right


    
class Solution :
    def sameTree (self, tree1 : Optional[TreeNode], tree2 : Optional[TreeNode]):
        
        def __fn (p, q):
            if not p and not q :
                return True 
            
            if not p or not q :
                return False
            
            if p.val != q.val:
                return False 
            else:
                return __fn(p.right, q.right) and __fn(p.left, q.left)
            
        return __fn(tree1, tree2)
    

    