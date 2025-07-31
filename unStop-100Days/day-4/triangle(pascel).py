def pascelTriangle (row : int) -> list:
    result = [1] * (row )
    ele, n = 1, row -1 
    for i in range(row):
        if i == 0 or i == row - 1:
            pass 
        else:
            ele = (ele * n) / i 
            result[i] = int(ele)
            n -= 1 
    
    return result 


print(pascelTriangle(5))

        