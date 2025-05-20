from collections import defaultdict
from INFalienIQ import * 
def top_K_freq_elem(numbers : list, K : int ) -> list:
    topK = []
    refDict = defaultdict(list)
    for value in set(numbers):
        ctr = numbers.count(value)
        refDict[ctr].append(value)
    refe = sorted(refDict.items(),key= lambda item : item , reverse = True )
    print(refe)
    for i in range(K):
        topK.append(refe[i][1])
    print(topK)
    return f"thezx"  



n = alien_generate(100, 0, 10)
print(top_K_freq_elem(n, 3))

