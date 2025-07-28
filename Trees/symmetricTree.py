from typing import Optional

class TreeNode:
    
    def __init__(self, val = 0, left = None , right = None ):
        self.val = val 
        self.left = left 
        self.right = right 

    def insertNode (self, root , node : int ):           
        if root.val < node:                              
            if self.right:                               
                return self.insertNode(root.right, node) 
            else:                                        
                root.right = TreeNode(node)              
                                                         
        elif root.val > node:                            
            if root.left:                                
                return self.insertNode(root.left, node)  
            else:                                        
                root.left = TreeNode(node)               
        else:                                            
            pass                                         
                                                         
        return root                                      

class Solution:
    def __str__(self) -> str:
        return f"class Solution is being called"

    def isSymmetric (self, treeStr : Optional[TreeNode]) -> bool:

        if not treeStr:
            return False

        def __fn(leftVal, rightVal):
            if not leftVal and not rightVal:
                return True

            if not leftVal or not rightVal:
                return False 

            if leftVal.val != rightVal.val :
                return False

            return __fn(leftVal.left, rightVal.right) and __fn(leftVal.right, rightVal.left)

        return __fn(treeStr.left, treeStr.right)

eles = [1,2,2,3,4,4,3]

root = TreeNode(eles[0])
for i in range(1, len(eles)):
    root.insertNode(root, eles[i])

def inorderTraversal (node, level = 0, prefix = "root:"):  
    if node:                                               
        print(f"{node.val}", end =" --")                   
        inorderTraversal(node.left)                        
        inorderTraversal(node.right)                       

inorderTraversal(root)
cs = Solution()
print(cs.isSymmetric(root))















