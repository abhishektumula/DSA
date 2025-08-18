# problem 11 : https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=greedy
# uses two pointer and greddy algo 
# making optimal decission in each step of the process results in globall optimization...

from typing import List


def MostWateraContainer (heights : List[int]) -> int:
    if not heights:
        return 0 
    maxArea = 0 
    i, j = 0, len(heights) - 1  # using two-pointer
    while i < j:
        currentArea = min(heights[i], heights[j]) * abs(i - j)
        if currentArea > maxArea:
            maxArea = currentArea

        if heights[j] > heights[i]:
            i += 1
        else: 
            j -= 1

    return maxArea


x = MostWateraContainer
print(x([1,8,6,2,5,4,8,3,7]))


