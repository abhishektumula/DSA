
from typing import List, Union


def solution(nums : List) -> Union[List, int] :
    print(nums)
    nums.sort() 
    print(nums)
    i, j = 0 ,len(nums) - 1
    while i <= j:
        subarray = nums[i : j + 1]
        if sum(subarray) == 0:
            print(subarray)
            return len(subarray)
        elif sum(subarray) <  0:
            i += 1 
        else:
            j -= 1 

    return -1 

print(solution([1, 2, -3, 3, -1, 2, -2]))


