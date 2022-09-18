# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

import re


def exist(board, word) -> bool:  

    def backtrack(curr, i, j):

        if curr == word:
            res.append(curr[:])
        
        if len(curr) == len(word):
            if res:
                return
        
        if i-1>=0 and board[i-1][j] == word[len(curr)]:
            letter = board[i-1][j]
            board[i-1][j] = 0
            backtrack(curr+letter, i-1, j)
            board[i-1][j] = letter

        if i+1<=m-1 and board[i+1][j] == word[len(curr)]:
            letter = board[i+1][j]
            board[i+1][j] = 0
            backtrack(curr+letter, i+1, j)
            board[i+1][j] = letter
            
        if j-1>=0 and board[i][j-1] == word[len(curr)]:
            letter = board[i][j-1]
            board[i][j-1]= 0
            backtrack(curr+letter, i, j-1)
            board[i][j-1] = letter

        if j+1<=n-1 and board[i][j+1] == word[len(curr)]:
            letter = board[i][j+1]
            board[i][j+1] = 0
            backtrack(curr+letter, i, j+1)
            board[i][j+1] = letter       
        
        

    curr = ""
    m = len(board)
    n = len(board[0])
    res = []
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                board[i][j] = 0
                backtrack(word[0], i, j)
                if res:
                    break
                board[i][j] = word[0]         
    if res:
        return True
    else:
        return False
   

board = [["a", "a"]]
word  = "aaa"

print(exist(board, word))