import time
import random
def product_except_itself(numbers : list) -> list :
    start_time = time.time()
    result_array = [1] * len(numbers)
    #calucate forward multiplication
    for i in range (1, len(numbers)):
        result_array[i] = result_array[i-1] * numbers[i-1]
    #calculate backward multiplicationion
    resulted_array = [1] * len(numbers)
    for i in range(len(numbers)-2, -1, -1):
        resulted_array[i] = resulted_array[i+1] * numbers[i+1]
    
    result = [] 
    for i in range(len(numbers)):
        result.append(result_array[i] * resulted_array[i])
# this approcah contains 3 for loops which leads to high time complexity
# but still better than using iterating in single for loop for len(numbers) times
    end_time = time.time()
    print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
    return result

def product_except_itself_optimized(numbers : list) -> list:
    start_time = time.time()
    result_array = [1] * len(numbers)
    for i in range(1, len(numbers)):
        result_array[i] = result_array[i-1] * numbers[i-1]
    prev = 1 
    for i in range(len(numbers)-1, -1, -1):
        result_array[i] = prev * result_array[i]
        prev *= numbers[i]
    end_time = time.time()
    print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
    return result_array

n = []
for _ in range(50):
    n.append(random.randint(1,7))


print(product_except_itself(n))
print(product_except_itself_optimized(n))
