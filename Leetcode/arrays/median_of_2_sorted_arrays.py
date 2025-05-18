# time complexity : O(log(m+n))
# 1. combine arrays and sort 
import random
from runtime import runtime 
import time
def media_sorted_array(arr1 : list, arr2 : list) -> list:
    start_time = time.time()
    arr1.extend(arr2)
    #print(arr1)
    n = len(arr1)
    if n % 2 == 0:
        ans = ((arr1[n//2] + arr1[(n//2)-1])/2)
        end_time = time.time()
        print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
        return ans
    else:
        ans = arr1[n//2]
        end_time = time.time()
        print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
        return ans
        

n1= []
for _ in range(100):
    start_time = time.time()
    n1.append(random.randint(-100,100))
    end_time = time.time()
print(f"-->{runtime(start_time, end_time)}")
n2= []
for _ in range(100):
    n2.append(random.randint(-100,100))


print(media_sorted_array(n1, n2))

