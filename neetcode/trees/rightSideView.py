from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ele = []
        rooto = root
        while root:
            ele.append(root.val)
            root = root.right

        return ele
