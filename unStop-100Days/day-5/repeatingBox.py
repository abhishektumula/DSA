from collections import Counter
def repeatingBox (nums : list) -> int:
    ctr = Counter(nums)
    for k, v in ctr.items():
        if v == len(nums) // 2:
            return k 
        
    return - 1


n = int(input())
num = list(map(int, input().split()))
print(repeatingBox(nums=num))