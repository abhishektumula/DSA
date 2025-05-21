import time 
from fucker import *
def solution(numbers :list) -> list:
    start_time = time.time()
    forward = [1] * len(numbers)
    for i in range(1, len(numbers)):
        forward[i] = forward[i-1] * numbers[i-1]
    #print(numbers)
    #print(forward)
    prev = 1 
    for i in range(len(numbers)-1, -1, -1):
        forward[i] *= prev 
        prev *= numbers[i]

    end_time = time.time()
    print(runtime(start_time, end_time))
    return forward
print(solution([1,2,3,4,5,6]))

