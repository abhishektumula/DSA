
import re
from typing import List

def diStringMatch(s : str) -> List[int]:
    if not s:
        return [] 

    # s = "IDID", output is  = [0,4,1,3,2]
    mainSet = [i for i in range(len(s) + 1)]
    result = []
    i_count, d_count = 0, len(s)  
    i = 0
    while i < len(s):
        if s[i] == "I":
            result.append(i_count)
            mainSet.remove(i_count)
            i_count += 1 
        else:
            result.append(d_count)
            mainSet.remove(d_count)
            d_count -= 1
        
        i += 1 

    if mainSet:
        result.extend(mainSet)

    return result 


print(diStringMatch("IDID")) #[0,4,1,3,2] 
print(diStringMatch("III"))  # [0,1,2,3]
print(diStringMatch("DDI"))  # [3,2,0,1]





