# runtime calculator to measure complexity
#
#INFalienIQ
import time 
import random
def runtime(start_time, end_time):
    return f"runtime:{(end_time - start_time)* 1000:.3f}ms"

def generate(n : int, start:int  , end : int  ) -> list:
    n = [random.randint(start,end) for _ in range(n)]
    print(n )
    return n
