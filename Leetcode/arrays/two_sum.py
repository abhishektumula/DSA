# approach 1 : brute force
import time
import random
def two_sum(numbers : list, target : int) -> list:
    start_time = time.time()
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i]  + numbers[j] == target:
                end_time = time.time()
                print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
                return [i,j]
    end_time = time.time()
    print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
    return False 

# this one actually works , 
# THIS WONT SUCK AS SHIT, I PROMISE
def fucker(numbers : list, target : list ) -> list:
    numbers.sort()m, if we fix one of the numbers, say x, we have to scan the entire array to find t
    start_time = time.time()
    for i in range(len(numbers)):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        x = numbers[i]
        tofind = target - x 
        toindex = numbers.index(tofind)
        if tofind :
            end_time = time.time()
            print(f"runtime: {(end_time - start_time)*1000:.3f}ms")
            return [i, toindex]

    end_time = time.time()
    print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
    return False
            
#THIS IS ONE OF THE SHITTIEST CODE I WROTE :) 
#THIS IS FUCKED UP
#THIS WILL WORK BUT WORKS AS SHIT
def two_sum_optimized(numbers :list, target : int) -> any:
    numbers.sort()
    start_time = time.time()
    map = set(numbers)
    hashindex = {i : [] for i in range(len(numbers))}
    for each in range(len(numbers)):
        hashindex[each].append(numbers[each])
    for i in range(len(numbers)):
        x = numbers[i]
        tofind = target - x  
        if tofind in map:
            for k,v in hashindex.items():
                if tofind in v:
                    end_time = time.time()
                    print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
                    return [i,k]
    end_time = time.time()
    print(f"runtime:{(end_time - start_time)*1000:.3f}ms")

    return False


n = []
for _ in range(100):
    n.append(random.randint(0,20))

print(two_sum(n, 9))
print(fucker(n,9))
print(two_sum_optimized(n, 9))

