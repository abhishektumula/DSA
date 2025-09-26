from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List:
        if not root:
            return []
        que = deque()
        levels = []
        que.append(root)
        while que:
            n = len(que)
            level = []
            for _ in range(n):
                node = que.popleft()
                level.append(node.val) if node else None
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            levels.append(level)

        return levels
