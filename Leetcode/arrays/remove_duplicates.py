# remove duplicates from sorted list 
import random
from runtime import runtime
import time 
# sets takes less time
# O(1) for adding, set() 
# index doesnt work in sets
def remove_duplicates(numbers : list ) -> list:
    start_time = time.time()
    ans = set(numbers)
    end_time = time.time()
    print(runtime(start_time,end_time))
    return list(ans)
# arrays take more time than sets 
# 0(n) for for loop, O(n) for search and O(n) for append

def remove_duplicates_array(numbers : list ) -> list:
    start_time = time.time()
    ans = []
    for each in numbers:
        if each not in ans:
            ans.append(each)
    end_time = time.time()
    print(runtime(start_time,end_time))
    return ans

n = [random.randint(0,10) for _ in range(500)]
print(f"-->{n}<--")
print(remove_duplicates(sorted(n)))
print(remove_duplicates_array(sorted(n)))

