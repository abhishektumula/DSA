
from typing import List, Any

def arrayPairSum (nums : List[int]) -> Any:
    nums.sort()
    n = len(nums)//2 
    currentSum = 0
    for i in range(0, len(nums), 2):
        currentSum += min(nums[i:i+2])

    return currentSum


print(arrayPairSum([1,2,3,4]))
print(arrayPairSum([6,2,6,5,1,2]))

