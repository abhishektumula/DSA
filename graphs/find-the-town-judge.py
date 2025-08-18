


from collections import defaultdict
from typing import List


class Solution:

    def findJudge (self, n : int, trust : List[List[int]]):
        _trust = defaultdict(int)
        trusts = set()
        for a, b in trust:
            _trust[b] += 1
            trusts.add(a) 


        for i, j in _trust.items():
            if i not in trusts and j == n -1:
                return i 


icl = Solution()
print(icl.findJudge(4,[[1,625], [2, 6250], [625, 1810],[2308, 1810] ]))
