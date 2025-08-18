

from typing import List


class Solution:
    
    def maxChunksToSorted(self, nums : List) -> int:
        if len(nums) == 1:
            return 1
        flag = 0 if nums[0] >= nums[1] else 1
        chucks = 0 
        for i in range(1,len(nums)):
        
