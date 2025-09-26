from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = 0
        curProduct = 1
        for i in range(len(nums)):
            curProduct *= nums[i]
            maxProduct = max(maxProduct, curProduct)
            if curProduct < 1:
                curProduct = 1

        return maxProduct


cl = Solution()
print(cl.maxProduct([2, 3, -2, 4]))
