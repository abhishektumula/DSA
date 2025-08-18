from typing import List

def largestPerimeter(nums : List[int]) -> int:
    if len(nums) < 3:
        return 0

    for i in range(len(nums) - 1, -1, -1):
        largest = nums[i]
        left, right = i - 2, i - 1
        while left >= 0:
            if nums[left] + nums[right] > largest:
                return nums[left] + nums[right] + largest
            elif left == 0:
                right -= 1 
                left = right - 1
            else:
                left -= 1 

    return 0
print(largestPerimeter([1,2,2]))
print(largestPerimeter([11,2,20,10]))
print(largestPerimeter([3,2,3,4]))
print(largestPerimeter([1,2,1,10]))
print(largestPerimeter([3,6,2,3]))

