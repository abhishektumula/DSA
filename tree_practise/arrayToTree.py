from typing import Optional, List
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right


class Solution:

    def arrayToTree (self, values : List) -> Optional[TreeNode]:

        def insertToTree (root : Optional[TreeNode], childs : int):
            if childs > root.val:
                if root.right:
                    return insertToTree(root.right, childs)
                else:
                    root.right = TreeNode(childs) 

                return root
            elif childs < root.val:
                if root.left:
                    return insertToTree(root.left, childs)
                else:
                    root.left = TreeNode(childs)

                return root

            return root
            

        root = TreeNode(values[0])
        for i in range(1, len(values)):
            insertToTree(root, values[i])

        tabs ="     "
        def inorder(node, level = 0, prefix = "ROOT : --> ") :
            if node:
                inorder(node.left, level=level + 1, prefix="L -->")
                print(f"{tabs * level} {prefix} {str(node.val)}")
                inorder(node.right, level= level+ 1, prefix="R -->")
            

        return inorder(root)
    


s = Solution()

print(s.arrayToTree([1,2,4,3,7,6,5,8,9,10]))
