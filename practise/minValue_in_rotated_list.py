import time 
from abhishek import * 
import heapq
def norm(numbers: list)-> int:
    start_time = time.time()
    res = min(numbers)
    end_time = time.time()
    print(runtime(start_time, end_time))
    return res

def using_heap(numbers : list) -> int:
    start_time = time.time()
    heapq.heapify(numbers)
    end_time = time.time()
    print(runtime(start_time, end_time))
    return numbers[0]

n = generate(1000000, 5, 400)
print(norm(n))
print(using_heap(n))
