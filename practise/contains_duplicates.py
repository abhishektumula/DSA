import time 
from INFalienIQ import * 
def contains_duplicates(numbers : list ) -> bool:
    map = set()
    start_time = time.time()
    for each in numbers:
        if each in map:
            end_time = time.time()
            print(alien_runtime(start_time, end_time))
            return True 
        else:
            map.add(each)
    end_time = time.time()
    print(alien_runtime(start_time, end_time))
    return False 

print(contains_duplicates(alien_generate(100, 0,10)))


