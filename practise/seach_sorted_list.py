#TODO: Find the optimal way to find the index 
#TODO: fuckin do something  
#TODO: 
#NOTE: can't do this now , just use .index()
#NOTE: fuck it, I'll find solution no matter what....!
import time
from abhishek import *
def solution(number : list, target: int ) -> int:
    start_time = time.time()
    found = number.index(target)
    end_time = time.time()
    print(runtime(start_time, end_time))
    return found

print(solution([3,4,5,6,1,2], 1))


