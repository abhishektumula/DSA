
from typing import List


class Solution:
    def minOper(self, N : int, arr) -> int:
        operaions = 0
        for i in range(len(arr)):
            each = arr[i]
            if each == 0:
                pass 
            elif each < 0 and abs(each) % 2 == 0:
                operaions += abs(each) /2 
                arr[i] = 0
            elif each > 0:
                operaions += each 
                arr[i] = 0
            else:
                pass
        if all(x == 0 for x in arr):
            return int(operaions )
        return -1

    def fn(self) -> int:
        N = int(input())
        arr = list(map(int, input().split()))
        result = self.minOper(N, arr)
        return result 
    


cl = Solution() 
print(cl.fn())
