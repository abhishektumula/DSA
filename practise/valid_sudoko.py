def valid_sudoko(board : list) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    sub_grid = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            act = board[i][j]
            if board[i][j] == ".":
                continue

            sub_index = ( i // 3)* 3 + (j // 3)
            if act in rows[i] or act in cols[j] or sub_index in sub_grid:
                return False 
            
            rows[i].add(act)
            cols[j].add(act)
            sub_grid[sub_index].add(act)

    return True 

print(valid_sudoko(#input))
