from collections import defaultdict
def chocolateShop (ques : list) -> None :
    items = defaultdict(int)
    for each in ques:
        if each[0] == "1":
            if each[1] not in items:
                items[each[1]] = 0 
            items[each[1]] += int(each[2])

        else:
            available = items[each[1]]
            if available >= int(each[2]):
                print(each[2])
                items[each[1]] -= int(each[2])
            else:
                print(available)

n = int(input())
queries = []
for _ in range(n):
    ele = list(map(str, input().split()))
    queries.append(ele)

chocolateShop(queries)
