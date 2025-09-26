class Solution:
    def triangleNumber(self, nums) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 1, -1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += abs(l - r)
                    r -= 1
                else:
                    l += 1
        return count


cl = Solution()
print(cl.triangleNumber([2, 2, 3, 4]))
