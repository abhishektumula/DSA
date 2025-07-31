def posterPrinter (order : str , l : int) -> bool:
    if l < 2:
        return False
    i = 0
    while i < l:
        if order[i] == "W":
            i += 1
            continue 

        j = i 
        hasB = hasR = False 
        while j < l and order[j] != "W":
            if order[j] == "R":
                hasR = True 
            
            if order[j] == "B":
                hasB = True 

            j += 1

        if not (hasR and hasB):
            return False 

        i = j
    return True


t = int(input())    
for _ in range(t):
    n, wd = int(input()), str(input())
    print(posterPrinter(wd, n))



