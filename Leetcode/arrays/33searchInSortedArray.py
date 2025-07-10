from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(mainPart: List[int], target: int) -> int:
            i, j = 0, len(mainPart) - 1
            while i <= j:
                mid = (i + j) // 2
                if mainPart[mid] == target:
                    return mid
                elif mainPart[mid] < target:
                    i = mid + 1
                else:
                    j = mid - 1
            return -1

        if not nums:
            return -1


        if nums[0] <= nums[-1]:
            return binarySearch(nums, target)


        def findPivot():
            # i, j = 0, len(nums) - 1
            # while i < j:
            #     mid = (i + j) // 2
            #     if nums[mid] > nums[j]:
            #         i = mid + 1
            #     else:
            #         j = mid
            value = min(nums)
            i = nums.index(value)
            return i

        pivot = findPivot()


        if nums[pivot] <= target <= nums[-1]:
            result = binarySearch(nums[pivot:], target)
            if result != -1:
                return result + pivot
        else:
            result = binarySearch(nums[:pivot], target)
            if result != -1:
                return result

        return -1


cls = Solution()
print(cls.search([4,5,6,7,0,1,2], 4))
print(cls.search([1], 4))
print(cls.search([4,5,6,7,0,1,2], 4))
print(cls.search([4,5,6,7,0,1,2], 4))
print(cls.search([4,5,6,7,0,1,2], 4))