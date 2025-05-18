# given an array , return all triplets i,j,k where i!=j!=k and
# i + j + k == 0
#
#approach - 1: Bruteforce 
#hight time complexity , 0(n) for each for loop -> 0(n)^3
import time
import random
def three_sum(number : list)-> list:
    start_time = time.time()
    res = [] 
    for i in range(len(number) - 3):
        for j in range(i+1,len(number) - 2):
            for k in range(j+1, len(number) - 1):
                if number[i] + number[j] + number[k] == 0:
                    ans = []
                    ans.append(number[i])
                    ans.append(number[j])
                    ans.append(number[k])
                    ans.sort()
                    if ans not in res:
                        res.append(ans)
    end_time = time.time()
    print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
    return res

def three_sum_optimized(number : list ) -> list: 
    res = []
    start_time = time.time()
    number.sort()
    for i in range(len(number)):
        if i > 0 and number[i] == number[i-1]:
            continue

        const = number[i]
        i, j = i, len(number) - 1 
        while i < j:
            threeSum = const + number[i] + number[j]
            if threeSum > 0 :
                j -= 1 
                while number[j] == number[j+1]:
                    j -= 1
            elif threeSum < 0:
                i += 1
                while number[i] == number[i-1]:
                    i += 1 
            else:
                res.append([const, number[i],number[j]])
                i += 1 
                while number[i] == number[i-1]:
                    i += 1 
                j -= 1 
                while number[j] == number[j+1]:
                    j -= 1 
    end_time = time.time()
    print(f"runtime:{(end_time - start_time)*1000:.3f}ms")
    return res

n = [ ]
for i in range(100):
    n.append(random.randint(-10,10))
#print(n)
print(three_sum_optimized(n))
print(three_sum(n))
