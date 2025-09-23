
from collections import Counter

def validAnagarm(s : str , t : str) -> bool:
    if not s and not t:
        return True 
    if not s :
        return False 
    if not t:
        return False 
    
    s_counter = dict(Counter(s))
    t_counter = dict(Counter(t))
    if len(s_counter) != len(t_counter):
        return False
    for k, v in s_counter:
        if s_counter[k] != t_counter[k]:
            return False 

    return True 









