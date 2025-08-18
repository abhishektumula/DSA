
from typing import List, Union
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits : List[int]) -> int:
        # edge case, when the len(fruits) == 1 : reutrn 1
        if len(fruits) == 1: return 1
        maxFound = 0
        for i in range(len(fruits)):
            for j in range(i + 1, len(fruits)):
                act = fruits[i : j + 1]
                if len(set(act)) <= 2:
                    maxFound = max(maxFound, len(act))

        return maxFound

cl = Solution()
print(cl.totalFruit([1,2,1]))
print(cl.totalFruit([0,1,2,2]))
print(cl.totalFruit([1,2,3,2,2]))
