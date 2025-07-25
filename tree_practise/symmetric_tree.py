from typing import Optional, Union
class TreeNode:
    def __init__(self, val = 0 , left = None , right = None):
        self.val = val 
        self.left = left 
        self.right = right


class Solution :
    # symnnetric : left half and rigth half should be mirror images...
    def isSymmetric (self, treeStr : Optional [TreeNode]) -> Union[bool, str, int]:
        
        if not treeStr:
            return True 
        
        def __fn (p, q):
            if not p and not q:
                return True 
            
            if not p or not q:
                return False 
            
            if p.val != q.val: return False 

            return __fn(p.left, q.right) and __fn(p.right, q.left)
        

        return __fn(treeStr.left, treeStr.right)
    

