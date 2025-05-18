# given an array , return all triplets i,j,k where i!=j!=k and
# i + j + k == 0
#
#approach - 1: Bruteforce 
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

n = [ ]
for i in range(100):
    n.append(random.randint(-10,10))
print(n)
print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum(n))
