# 3 3
# 1 2 3
# 4 5 6
# 7 8 9

# sample op : 1 2 3 6 9 8 7 4 5


def hereComes(path : list[list]) -> list:
    n, m = len(path), len(path[0])
    result = set()
    if len(path) == 1:
        result.extend(path)
        return result
    
    direction = "row"
    goFurther = True
    ci, cj = 0, 0
    while goFurther:
        if path[ci][cj] in result and path[ci+1][cj] in result:
            goFurther = False
        
        if direction == "row":
            while cj < len(m):
                if path[ci][cj] not in result:
                    result.add(path[ci][cj])
                    cj += 1
                else:
                    if ci == n - 1:
                        ci -= 1
                    ci += 1
