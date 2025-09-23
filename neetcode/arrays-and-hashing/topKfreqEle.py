
from typing import List


def topKele (nums : List, k : int) :
    counter = {} 
    for each in nums:
        if each not in counter:
            counter[each] = 0 
        counter[each] += 1
    result = list(filter(lambda x : x[1] >= k , list(counter.items() )))
    xx =[] 
    for i in result:
        xx.append(i[0])
    return xx 

print(topKele([1,2,2,2,3,3,4, 4,4], 2))


