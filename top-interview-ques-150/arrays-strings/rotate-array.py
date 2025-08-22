
from typing import List


class Solutioin:

    def rotateArray (self, nums: List[int], n : int) -> List[int]:

        n = n % len(nums)
        
        for _ in range(n):
            nums.insert(0, nums.pop())

        return nums


cl = Solutioin() 
print(cl.rotateArray([1,2,3,4,5,6,7], 3))

