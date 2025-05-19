import time
import random
from runtime import runtime
def remove_element(numbers : list, target : int ) -> list:
    start_time = time.time()
    res = []
    for value in numbers: 
        if value != target:
            res.append(value)

    end_time = time.time()
    print(runtime(start_time, end_time))
    return res


n = [random.randint(1,10) for _ in range(100)]
print(remove_element(n, 7))


