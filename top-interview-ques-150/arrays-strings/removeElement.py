
from typing import List

class Solution:
    def removeElement (self, nums : List[int], value : int) -> int:
        if not nums:
            return 0 
        i = 0
        while i < len(nums):
            if nums[i] == value:
                nums.pop(i) 
            else:
                i += 1 

        print(nums)
        return len(nums)

cl = Solution()

print(cl.removeElement([3,2,2,3], 3))
