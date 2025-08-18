from typing import List

def canPlaceFlowers (nums : List, target : int) -> int:
    if not nums: return True
    i = 0
    ctr = 0
    while i < len(nums):
        if nums[i] == 0:
            if i == 0 and len(nums) > 1:
                if nums[i+1] == 0 and nums[i] == 0:
                    ctr += 1
                    nums[i] = 1 
                    i += 1
            elif i == len(nums) -1:
                if nums[i-1] == 0:
                    ctr += 1 
                    nums[i] = 1 

            else:
                if nums[i+1] == 0 and nums[i-1] == 0 :
                    ctr += 1 
                    nums[i] = 1
                    i += 1
            
            i += 1
        else:
            i += 1
    return ctr >= target

print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([], 1))
