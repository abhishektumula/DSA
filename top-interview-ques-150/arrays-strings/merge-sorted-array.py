import time 
from typing import List
class Solution:
    
    def merge (self, nums1 : List[int], m : int, nums2 : List[int], n : int ) -> List[int]:
        i =  0
        while len(nums1) != m:
            if nums1[i] == 0:
                nums1.pop(i)
            else:
                i += 1 

        nums1.extend(nums2)
        return sorted(nums1, reverse=False)


cl = Solution()
print(cl.merge([1,2,3,0,0,0], 3, [1,2,6], 3))


