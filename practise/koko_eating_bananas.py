import time 
from abhishek import runtime, generate 
# TODO: find maximum and minimum from list
# TODO: statrt loop from min to max and find hours < target hours
# TODO: return the minimum eating rate 
# 
# TODO: Optimze this shit before anyone sees it 
# NOTE: i am not done yet 

import math 
def kok0_bananas(piles : list, h : int) -> int:
    res = []
    start_time = time.time()
    a, s = max(piles), min(piles)
    for i in range(1, a+1):
        total = 0 
        for each in piles:
            total += math.ceil(each/i)
        if total <= h :
            res.append(i)

    end_time = time.time()
    print(runtime(start_time, end_time))
    return min(res) if res else None 

print(kok0_bananas([1,4,3,2], 9))
print(kok0_bananas([3,6,7,11], 8))
print(kok0_bananas([30], 5))
n = generate(100, 1, 10)

