
from typing import List 

class Solution:

    def removeDuplicates (self, nums: List[int]) -> int:
        if not nums:
            return 0 
        if len(nums) == 1:
            return 1 
        result = [nums[0]]
        i = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                result.append(nums[i])
                i += 1 
            else:
                nums.pop(i)

        print(nums)
        return len(result)


cl = Solution()
a = [1,2,1,1,3,4,4,2,3,4,1,2,4,5]
print(cl.removeDuplicates(sorted(a)))
