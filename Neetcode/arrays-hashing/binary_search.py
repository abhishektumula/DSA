from typing import Union
import time
import random
def binary_search(numbers : list, target : int) -> Union[int, bool]:
    numbers.sort()
    i, j = 0, len(numbers) - 1
    start_time = time.time()
    while i <= j:
        midindex = (i + j ) //2  
        midvalue = numbers[midindex]
        if midvalue == target:
            end_time = time.time()
            print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
            return midindex
        elif midvalue > target:
            j = midindex - 1
        else:
            i = midindex + 1
    end_time = time.time()
    print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
    return False

def array_generator(size : int)->list:
    result = []
    for _ in range(size):
        result.append(random.randint(0,100))

    return sorted(result)
n = array_generator(200)
print(n)
print(binary_search(n, 99))


