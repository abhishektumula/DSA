
from typing import List
class Solution:
    def areaOfMaxDiagonal(self, dim : List) -> int:
        diag = float('-inf')
        for each in dim:
            res = pow(each[0], 2) + pow(each[1], 2)
            if int(pow(res, 0.5)) > diag:
                diag = int(pow(res, 0.5))

        return int(diag)









