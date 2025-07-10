from typing import List
import time
import random
def prodcutExpectSelf (nums : List) -> List:
    start_time = time.time()
    result = [0] * len(nums)
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]

        result[i] = product
    end_time = time.time()
    print(f"runtime :: {(end_time - start_time) * 1000:.3f}")
    # return result

def productExpectSelf2 (nums : List) -> List:
    start_time = time.time()
    forward = [1] * len(nums)
    for i in range(1, len(nums)):
        forward[i] = forward[i-1] * nums[i-1]

    backward = [1] * len(nums)
    for i in range(len(nums)-2, -1, -1):
        backward[i] = backward[i+1] * nums[i+1]

    res = [1] * len(forward)
    for i in range(len(forward)):
        res[i] = forward[i] * backward[i]
    
    end_time = time.time()
    print(f"runtime :: {(end_time - start_time) * 1000:.3f}")
    # return res

def productExceptSelf3 (nums : List) -> List:
    start_time = time.time()
    forward = [1] * len(nums)

    for i in range(1,len(nums)):
        forward[i] = forward[i-1] * nums[i-1]

    prev = 1
    for i in range(len(nums)-1, -1, -1):
        forward[i] *= prev 
        prev *= nums[i]
    
    end_time = time.time()
    print(f"runtime :: {(end_time - start_time)*1000:.3f}")
    # return forward


n = [random.randint(1,10) for _ in range(10000)]

print(prodcutExpectSelf(n))
print(productExpectSelf2(n))
print(productExceptSelf3(n))




