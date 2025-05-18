import random
def solution(numbers : list) -> int:
    numbers.sort()
    res = 0
    for each in numbers:
        m = each + 1
        ans = 1
        while m in numbers:
            ans += 1
            m += 1
        
        res = max(res, ans)

    return res

print(solution([1,2,3,4,5,100,201,202,203,204,205,206]))
n = []
for i in range(100):
    n.append(random.randint(0,100))
print(sorted(n))
print(solution(n))

