

class Solution:
    def pathSum(self, root : Optional[TreeNode], target) -> bool:
        
        def fuckYou(node, cs):
            if not node:
                return False 
            
            cs += node.val 

            if not node.left and not node.right:
                return cs == target 

            return fuckYou(node.left,cs) or fuckYou(node.right, cs) 


        return fuckYou(root, cs=0)
