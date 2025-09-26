
from typing import List, Optional 

class TreeNode:
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.right , self.left = right, left 
class Solution:
    def arrayToBinary(self, nums : List[int]) -> Optional[TreeNode]:
        if not nums:
            return None 
        n = nums[len(nums) // 2]
        root = TreeNode(nums[n])

        root.left = self.arrayToBinary(nums[:n])
        root.right = self.arrayToBinary(nums[n+1:])

        return root

        



