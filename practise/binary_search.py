#TODO : Do something , get something
import time 
from abhishek import *
def binary_search(numbers : list, target : int) -> int:
    start_time = time.time()
    numbers.sort()
    i, j = 0, len(numbers) - 1
    while i <= j :
        midindex = (i + j) //2 
        midvalue = numbers[midindex]
        if midvalue == target:
            end_time = time.time()
            print(runtime(start_time, end_time))
            return midindex
        elif midvalue < target:
            i = midindex + 1
        else:
            j = midindex - 1
    end_time = time.time()
    print(runtime(start_time, end_time))
    return -1

n = generate(100, -10, 10)
print(binary_search(n,1))



