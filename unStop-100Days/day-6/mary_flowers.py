
def flower_indexes (n : int, flowers : list) -> list :
    if len(flowers) == 1 and n == flowers[0]:
        return flowers[0]
    i, j = 0, len(flowers) - 1
    while i < j :
        if flowers[i] + flowers[j] == n:
            return [i, j]
        elif flowers[i] + flowers[j] > n :
            j -= 1 
        else:
            i += 11




