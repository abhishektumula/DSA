

from collections import defaultdict
from typing import List

class Solution:
    def findCenter(self, edges : List) -> int:
        nNodes = defaultdict(int) 
        for i, j in edges:
            nNodes[i] += 1 
            nNodes[j] += 1
        for key, value in nNodes.items():
            if value == len(nNodes) - 1:
                return key 
        return -1 

cl = Solution() 
print(cl.findCenter([[1,2],[2,3],[4,2]]))
print(cl.findCenter([[1,2],[5,1],[1,3],[1,4]]))
