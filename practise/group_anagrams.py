from collections import defaultdict
def group_anagrams(names : list) -> any:
    cakes = defaultdict(list)
    for each in names:
        cups = [0] * 26
        for m in each:
            cups[ord(m) - ord('a')] += 1

        cakes[tuple(cups)].append(each)
    res = []
    for k, v in cakes.items():
        res.append(v)
    return res
print(group_anagrams(['cat', 'tac', 'sat', 'fuck', 'fcuk']))

