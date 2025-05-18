def top_k_frqEle(numbers : list, k : int ) -> any:
    counter = {i : [] for i in range(len(numbers), -1, -1)}
    face = set(numbers)
    for each in face:
        ctr = numbers.count(each)
        counter[ctr].append(each)
    clean = {k:v for k,v in counter.items() if v}
    result = list(clean.values())
    ans =[]
    for i in range(k):
        ans.extend(result[i])
    return ans
print(top_k_frqEle([1,2,3,4,5,5,6,7,7, 8,8,8,8,8,9], 2))
