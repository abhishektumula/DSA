import time 
from abhishek import *
def two_sum2(numbers : list, target : int) -> list:
    i, j = 0, len(numbers) - 1
    while i <= j:
        if numbers[i] + numbers[j] == target:
            org = j
            j -= 1
            while j != len(numbers) - 1 and numbers[j] == numbers[j+1]:
                j -= 1 
            org = min(org, j)
            return [i+1, org+2]
        elif numbers[i] + numbers[j] > target:
            j -= 1
            while j != len(numbers) - 1 and numbers[j] == numbers[j+1]:
                j -= 1
        else:
            i += 1
            while i > 0 and numbers[i] == numbers[i-1]:
                i += 1 

    return False 


print(two_sum2([1,2,3,4,5,5], 7))
