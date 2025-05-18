import random
import time
from runtime import runtime
def three_sum_closest(numbers : list, target : int) -> int:
    numbers.sort()
    start_time = time.time()
    for i in range(len(numbers)):
        res = max(numbers) 
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        const = numbers[i]
        x, y = i+1, len(numbers) - 1
        while x < y:
            current =  (const + numbers[x] + numbers[y])
            todiff = target - current
            if abs(todiff) < abs(res - target):
                res = current

            if todiff < 0:
                x += 1
                while x < y and numbers[x] == numbers[x-1]:
                    x += 1 
            else:
                y -= 1 
                while x < y and  numbers[y] == numbers[y+1]:
                    y -= 1
    end_time = time.time()
    print(runtime(start_time, end_time))
    return res


n = []
for _ in range(100):
    n.append(random.randint(-10,20))
fucker = random.randint(0, 10)
print(n, fucker)
print(three_sum_closest(n,fucker))
print(three_sum_closest([-1,2,1,-4], 1))
print(three_sum_closest([0,0,0], 1))


