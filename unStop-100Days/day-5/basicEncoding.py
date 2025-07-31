from collections import defaultdict
def basicEncoding (reps : list) -> int:
    ctr = defaultdict(int)
    for i,j in reps:
        ctr[j] += i 

    if len(ctr) < 2 :
        return 0 
    

    values = sorted(list(ctr.items()), key= lambda x : x[1])
    result = values[0][0] - values[-1][0]
    return abs(result)

if __name__ == "__main__":
    n = int(input())
    rep = []
    for _ in range(n):
        ele = list(map(int, input().split()))
        rep.append(ele)

    print(basicEncoding(rep))


