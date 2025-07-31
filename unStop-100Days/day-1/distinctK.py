# from collections import Counter
# def solution():
#     a = 10
#     res = ""
#     for _ in range(a):
#         res += input()

#     cts = dict(Counter(res))

#     result = []
#     for key,value in cts.items():
#         if value == 1:
#             result.append(key)
    
#     return result


# print(solution())
from itertools import product
a = [1,2]
ans =  (product(a, repeat =4))
print(list(ans))

