from collections import Counter
def freqSort (nums : list) -> list:
    result = []
    ctr = Counter(nums)
    print(f" counter {ctr}")
    print(sorted(ctr.items(), key=lambda x : x[1]))
    for ke, val in sorted(ctr.items(), key=lambda x : x[1], reverse=True):
        result.extend([ke] * val)  


    return result 



print(freqSort([6,2,4,3,4,6,1,2,4,4,4]))