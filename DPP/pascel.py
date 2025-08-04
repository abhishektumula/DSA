from typing import List


class Solution :
    def generateRow (self, number : int) -> List[int]:
        result = [1] * number
        ele, n = 1, number - 1
        for i in range(number):
            if i == 0 or i == number - 1:
                pass 
            else:
                ele = (ele *n) / i
                result[i] =  int(ele)
                n -= 1 

        return result 


    def pascelTrainagle (self, rows : int) -> List[List[int]]:
        if not rows:
            return [[0]]
        result = []
        for i in range(1, rows + 1):
            result.append(self.generateRow(i))
        
        return result



cl = Solution() 
print(cl.pascelTrainagle(5))


    
