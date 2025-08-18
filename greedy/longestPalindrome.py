import collections
from typing import List 
from collections import defaultdict

def longestPalindrome (s : str) -> int:
    counter = defaultdict(int)
    result = 0

    for each in s:
        counter[each] += 1 
        # if there are even pair then, increament the result by 2
        if counter[each] % 2 == 0:
            result += 2

    # if any odd pair found, then increament it by 1 and then break
    for cnt in counter.values():
        if cnt% 2:
            result += 1
            break

    return result



print(longestPalindrome('abccccdd'))
