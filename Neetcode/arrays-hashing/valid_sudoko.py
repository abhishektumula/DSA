def valid_sudoko(board : list[list]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrid = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            nums = board[i][j]
            if nums == ".":
                continue
            
            subindex = (i // 3) * 3 + (j // 3)

            if nums in rows[i] or nums in cols[j] or nums in subgrid[subindex]:
                return False 
            
            rows[i].add(nums)
            cols[j].add(nums)
            subgrid[subindex].add(nums)

    return True 

print(valid_sudoko(board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))
