
from typing import List
from itertools import combinations

def minMaxSum(nums : List[int], k : int):
    result =[]
    r = 1
    for i in range(1, k + 1 ):
        result.extend(list(combinations(nums, i)))
    result.sort()    
    result = sorted(result, key=lambda x: len(x))
    for eh in result:
        print(f"{r} =>{eh}")
        r += 1
    
minMaxSum([1,2,3,4,5,6,7,8,9,10], 3)









