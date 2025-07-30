from typing import List
from functools import reduce
class Solution:
    def andOperaion (self, a, b):
        return a&b

    def longestSubarray(self, nums : List[int]) -> int:
        finalres = 0
        subarray = []
        andValue = 0
        i = 0
        while i < len(nums):
            main = nums[i]
            subs = []
            j = i 
            while j < len(nums) and nums[j] == main:
                subs.append(nums[j])
                j += 1
            if len(subs) == 1:
                temp = subs[0]
            else:
                temp = reduce(self.andOperaion, subs) 

            if temp > andValue:
                andValue = temp
                finalres = len(subs)
            
            i = j

        return finalres

                 


cl = Solution()
# print(cl.longestSubarray([1,2,3,3,2,2]))
print(cl.longestSubarray([1,2,3,3,2,2]))
print(cl.longestSubarray([100, 5, 5]))
print(cl.longestSubarray([311155,311155,311155,311155,311155,311155,311155,311155,201191,311155]))


