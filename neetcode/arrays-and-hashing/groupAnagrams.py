
from typing import List
from collections import defaultdict

def groupAnagrams(eles : List[str]) -> List:
    result = []
    groups = defaultdict(list)
    for each in eles:
        ctr =[0] * 26 
        for ch in each:
            ctr[ord(ch) - 97] += 1 

        groups[tuple(ctr)].append(each)



    return list(groups.values())


print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
