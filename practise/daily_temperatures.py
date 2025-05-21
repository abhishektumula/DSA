#appraoach 1 : for - for loop
# approach 2 : for - while loop
# TODO : check runtime and optimze this shit before anyone notices
# TODO : don't fuck yourself ABHISHEK ...
import time 
from abhishek import *
def daily_temperature(summary : list) -> list:
    start_time = time.time()
    res = [0] * len(summary)
    for i in range(len(summary)):
       for j in range(i+1, len(summary)):
            if summary[i] < summary[j]:
                res[i]= (j - i)
                break

    end_time =  time.time()
    print(runtime(start_time, end_time))
    return res 

def daily_temperature_2(summary : list ) -> list:
    start_time = time.time()
    res = [0] * len(summary)
    for i in range(len(summary)):
        j = i + 1
        while j < len(summary):
            if summary[i] < summary[j]:
                res[i] = j - i 
                break 
            j += 1

    end_time = time.time()
    print(runtime(start_time, end_time))
    return res 

print(daily_temperature([30,38,30,36,35,40,28,43,12,23,45,76,34,54,23,76,56,20]))
print(daily_temperature_2([30,38,30,36,35,40,28,43,12,23,45,76,34,54,23,76,56,20]))
