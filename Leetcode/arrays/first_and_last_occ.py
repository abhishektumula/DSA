import time 
from runtime import runtime
def first_and_last_occ(numbers : list, target : int) -> list:
    start_time = time.time()
    i, j = 0, len(numbers) - 1
    res = []
    first , last =  -1 ,  - 1
    for i in range(len(numbers)):
        if numbers[i] == target:
            first = i 
            break 
    for j in range(len(numbers)-1, -1, -1):
        if numbers[j] == target:
            last = j 
            break
    end_time = time.time()
    print(runtime(start_time, end_time))
    return (first, last)
    
print(first_and_last_occ([5,7,7,8,8,10], 8))


