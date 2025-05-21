import time 
from abhishek import *
def threeSumOptimized(numbers : list) -> list:
    numbers.sort()
    res = []
    start_time = time.time()
    for i in range(len(numbers)):
        if i > 0 and numbers[i] == numbers[i-1]:
            continue

        main = numbers[i]
        x, y = i + 1, len(numbers) - 1
        while x < y:
            threeSum = main + numbers[x] + numbers[y]
            if threeSum == 0:
                res.append([main, numbers[x], numbers[y]])
                x += 1 
                y -= 1 
                while numbers[x] == numbers[x-1]:
                    x += 1
                while numbers[y] == numbers[y+1]:
                    y -= 1
            elif threeSum > 0:
                y -= 1 
                while numbers[y] == numbers[y+1]:
                    y -= 1 
            else:
                x += 1 
                while numbers[x] == numbers[x-1]:
                    x += 1 
    end_time = time.time()
    print(runtime(start_time, end_time))
    return " "
#    return res


def three_sum(numbers : list ) -> list:
    numbers.sort()
    res = []
    checked = set()
    start_time = time.time()
    for i in range(len(numbers)):
        if numbers[i] in checked:
            continue
        checked.add(numbers[i])

        x = numbers[i]
        y, z = i + 1, len(numbers) - 1
        while y < z :
            threeSum = x + numbers[y] + numbers[z]
            if threeSum == 0:
                res.append([x, numbers[y], numbers[z]])
                y += 1 
                z -= 1 
                while y > 0 and numbers[y] == numbers[y-1]:
                    y += 1 
                while z != len(numbers) - 1 and numbers[z] == numbers[z+1]:
                    z -= 1
            elif threeSum > 0:
                z -= 1
                while numbers[z] == numbers[z+1]:
                    z-=1
            else:
                y += 1
                while y > 0 and numbers[y] == numbers[y-1]:
                    y += 1 

    end_time = time.time()
    print(runtime(start_time, end_time))
    return " " 
#    return res

n = generate(200, -10, 10)
#print(f"-->{n}<--")
print(threeSumOptimized(n))
print(three_sum(n))
