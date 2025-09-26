from tarfile import TarError
from typing import List


class Solution:
    def combinationSum(self, nums: List, target: int) -> List:
        result = []

        def dfs(i, curr, totalSum):
            if totalSum == target:
                result.append(curr.copy())
                return
            if i >= len(nums) or totalSum > target:
                return

            curr.append(nums[i])
            dfs(i, curr, totalSum + nums[i])

            curr.pop()
            dfs(i + 1, curr, totalSum)

        dfs(0, [], 0)
        return result


cl = Solution()
print(cl.combinationSum([2, 3, 5, 7], 7))
