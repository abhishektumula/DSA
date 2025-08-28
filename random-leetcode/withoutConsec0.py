
import time 
class Solution:
    def findIntegers(self, number : int ) -> int:
        result = number
        start_time = time.time()
        for i in range(number + 1):
            if i & i >> 1:
                result -= 1 

        end_time = time.time()
        print(f"{(end_time - start_time) * 1000:.2f}ms")
        return result


cl = Solution()
print(cl.findIntegers(100000000))









