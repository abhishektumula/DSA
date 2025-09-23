from typing import List 

def twoSum(nums : List[int], target : int) -> List[int]:
    for i in range(len(nums)-1):
        find = target - nums[i]
        if find in nums[i+1:]:
            return [i, nums.index(find)]
    return [-1, -1]
