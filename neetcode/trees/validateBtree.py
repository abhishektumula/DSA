from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def validateBinaryTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        low, high = float("-inf"), float("inf")

        def validation(node, low, high):
            if not node:
                return False
            if not (node.val < high and node.val > low):
                return False

            return validation(node.left, low, node.val) and validation(
                node.right, node.val, high
            )

        return validation(root, low, high)
