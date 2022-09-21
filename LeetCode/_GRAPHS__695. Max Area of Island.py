# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

from collections import defaultdict



def maxAreaOfIsland(grid):

    ROWS, COLS = len(grid)-1, len(grid[0])-1

    area = 0
    maxArea = 0

    visited = set()

    def traverse(r, c, area):
        if ((r, c) in visited) or r<0 or r>ROWS or c<0 or c>COLS or grid[r][c] != 1:
            return area
        visited.add((r, c))
        area +=1
        area = traverse(r+1, c, area)
        area = traverse(r-1, c, area)
        area = traverse(r, c-1, area)
        area = traverse(r, c+1, area)

        return area

    for r in range(ROWS+1):
        for c in range(COLS+1):
            if ((r, c) not in visited) and grid[r][c]==1:                
                area = traverse(r, c, area)
                if area > maxArea:
                    maxArea = area
            
            area = 0            

    return maxArea

grid = [[0,0,1,],
        [1,1,0]]

print(maxAreaOfIsland(grid))