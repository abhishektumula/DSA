from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left, self.right = left, right


class Solution:
    def isSubTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            if p and q and p.val == q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            return False

        if not root2:
            return True
        if not root1:
            return False
        if sameTree(root1, root2):
            return True
        return sameTree(root1.left, root2) or sameTree(root1.right, root2)
