from typing import List 

class Solution:

    def removeDuplicates (self, nums: List[int]) -> int:
        if not nums:
            return 0 
        if len(nums) == 1:
            return 1 
        i = 2
        while i < len(nums):
            if nums[i] == nums[i-1] == nums[i-2]:
                nums.pop(i)
            else:
                i += 1
        print(nums)
        return len(nums)


cl = Solution()
a = [1,2,1,1,3,4,4,2,3,4,1,2,4,5]
print(sorted(a))
print(cl.removeDuplicates(sorted(a)))
print(cl.removeDuplicates([1,1,1,2,2,3]))
