from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def commonAncister(self, root: Optional[TreeNode], p: int, q: int) -> int:
        # assuming p and q are interger, if p and q are given as TreeNodes
        # replcae p with p.val and q with q.val
        def function(node, p, q):
            if p > node.val and q < node.val:
                return node.val
            if p < node.val and q > node.val:
                return node.val
            if p == node.val or q == node.val:
                return node.val
            if p > node.val and q > node.val:
                return function(node.right, p, q)
            else:
                return function(node.left, p, q)

        if not root:
            return False
        return function(root, p, q)
