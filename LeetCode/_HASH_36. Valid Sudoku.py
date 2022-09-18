# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.



def isValidSudoku(board) -> bool:

    rows = [[] for i in range(9)]
    cols = [[] for i in range(9)]
    squares = [[] for i in range(9)]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!='.':
                rows[i].append(board[i][j])


    for i in range(len(board)):        
        for j in range(len(board[i])):
            if board[i][j]!='.':
                cols[j].append(board[i][j])
    
    for i in range(3):
        for j in range(3):
            for x in range(3):
                for y in range(3):
                    if board[x + i*3][y + 3*j] != '.':
                        squares[i+j*3].append(board[x + i*3][y + 3*j])

    for row in rows:
        if len(set(row)) != len(row):
            return False
    
    for col in cols:
        if len(set(col)) != len(col):
            return False

    for square in squares:
        if len(set(square)) != len(square):
            return False

    return True


board1=[["8","3",".",".","7",".",".",".","."]
      ,["6",".",".","1","9","5",".",".","."]
      ,[".","9","8",".",".",".",".","6","."]
      ,["8",".",".",".","6",".",".",".","3"]
      ,["4",".",".","8",".","3",".",".","1"]
      ,["7",".",".",".","2",".",".",".","6"]
      ,[".","6",".",".",".",".","2","8","."]
      ,[".",".",".","4","1","9",".",".","5"]
      ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board1))

