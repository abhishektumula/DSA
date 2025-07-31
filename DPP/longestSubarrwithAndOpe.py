from typing import List
class Solution:
    def longestSubarray(self, numbers : List[int]) -> int:
        maxLength , currentLenght , endIndex = 0,0,0
        maxValue = max(numbers)
        for i, value in enumerate(numbers):
            if numbers[i] == maxValue:
                currentLenght += 1
                if currentLenght > maxLength:
                    maxLength = currentLenght
                    endIndex = i 

            else:
                currentLenght = 0

        return maxLength


cl = Solution()
