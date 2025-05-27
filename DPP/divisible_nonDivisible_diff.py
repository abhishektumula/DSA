#NOTE: itertate throught the loop, then find the dividibles and non-div
#NOTE: keep the track of sum using two varibales
#NOTE: find the abs difference and return stuff
#NOTE: find the optimal way... , btw i already found the optimal way

#TODO: just use your f brani..

import time 
def difference(rangeValue : int, div : int) -> int:
    start_time = time.time()
    if not rangeValue:
        return 0
    num1, num2 =0, 0
    for i in range(1,rangeValue+1):
        if i % div == 0:
            num1 += i 
        else:
            num2 += i 

    end_time = time.time()
    print(f"runtime: {(end_time - start_time)*1000:.3f}ms")
    return abs(num1 - num2)
#
#this is f working, its the optimal or one of the optimal way to find the solution
def difference_optimized(rangeValue: int, div:int) -> int:
    start_time = time.time()
    totalSum =  (rangeValue * (rangeValue + 1)) / 2 
    multipleSum = 0
    for i in range(1, (rangeValue//div) + 1 ):
        multipleSum  += i * div 
    end_time = time.time()
    print(f"runtime: {(end_time - start_time)*1000:.3f}ms")
    return abs((totalSum - multipleSum) - multipleSum )

print(difference(1000000,3))
print(difference_optimized(1000000,3))

