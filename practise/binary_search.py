#TODO : Do something , get something
import time 
from abhishek import *
def binary_search(numbers : list, target : int) -> int:
    numbers.sort()
    start_time = time.time()
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

def findIndex(n, m):
    n.sort()
    start_time = time.time()
    f = n.index(m)
    end_time = time.time()
    print(runtime(start_time, end_time))
    return f 


n = generate(1000000, -10, 10)
print(binary_search(n,1))
print(findIndex(n, 1))



