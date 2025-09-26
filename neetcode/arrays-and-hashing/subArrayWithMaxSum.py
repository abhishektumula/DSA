from typing import List


class Solution:
    def subArrayMaxSum(self, nums: List[int]) -> int:
        # kadane's algorithm
        maxSum = float("-inf")
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0

        return int(maxSum)


cl = Solution()
print(cl.subArrayMaxSum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
