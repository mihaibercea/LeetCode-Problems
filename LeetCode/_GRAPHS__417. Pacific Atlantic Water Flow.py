# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

# Example 1:


# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
# Example 2:

# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

# Constraints:

# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105

from calendar import TUESDAY
from collections import defaultdict



def pacificAtlantic(heights):

    ROWS, COLS = len(heights)-1, len(heights[0])-1

    result = []

    visited = set()   

    def checkFlowPacific(r, c, watered):
        if r == 0 or c == 0:
            return True
        else:
            if r-1>=0 and heights[r-1][c]<=heights[r][c] and (r-1, c) not in watered:
                watered.add((r-1, c))
                check = checkFlowPacific(r-1, c, watered)
                if check:
                    return check

            if r+1<=ROWS and heights[r+1][c]<=heights[r][c] and (r+1, c) not in watered:
                watered.add((r+1, c))
                check = checkFlowPacific(r+1, c, watered)
                if check:
                    return check

            if c-1>=0 and heights[r][c-1]<=heights[r][c] and (r, c-1) not in watered:
                watered.add((r, c-1))
                check = checkFlowPacific(r, c-1, watered)
                if check:
                    return check

            if c+1<=COLS and heights[r][c+1]<=heights[r][c] and (r, c+1) not in watered:
                watered.add((r, c+1))
                check = checkFlowPacific(r, c+1, watered)
                if check:
                    return check


    def checkFlowAtlantic(r, c, watered):
        if r == ROWS or c == COLS:
            return True
        else:
            if r-1>=0 and heights[r-1][c]<=heights[r][c] and (r-1, c) not in watered:
                watered.add((r-1, c))
                check = checkFlowAtlantic(r-1, c, watered)
                if check:
                    return check

            if r+1<=ROWS and heights[r+1][c]<=heights[r][c] and (r+1, c) not in watered:
                watered.add((r+1, c))
                check = checkFlowAtlantic(r+1, c, watered)
                if check:
                    return check

            if c-1>=0 and heights[r][c-1]<=heights[r][c] and (r, c-1) not in watered:
                watered.add((r, c-1))
                check = checkFlowAtlantic(r, c-1, watered)
                if check:
                    return check

            if c+1<=COLS and heights[r][c+1]<=heights[r][c] and (r, c+1) not in watered:
                watered.add((r, c+1))
                check = checkFlowAtlantic(r, c+1, watered)
                if check:
                    return check

    for r in range(ROWS+1):
        for c in range(COLS+1):
            if (r, c) not in visited:
                visited.add((r, c))                

                if checkFlowPacific(r, c, watered = set()) and checkFlowAtlantic(r, c,watered = set()):
                    result.append([r, c])

    return result

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
heights1 = [[ 8,13,11,18,14,16,16, 4, 4, 8,10,11, 1,19, 7],
            [ 2, 9,15,16,14, 5, 8,15, 9, 5,14, 6,10,15, 5],
            [15,16,17,10, 3, 6, 3, 4, 2,17, 0,12, 4, 1, 3],
            [13, 6,13,15,15,16, 4,10, 7, 4,19,19, 4, 9,13],
            [ 7, 1, 9,14, 9,11, 5, 4,15,19, 6, 0, 0,13, 5],
            [ 9, 9,15,12,15, 5, 1, 1,18, 1, 2,16,15,18, 9],
            [13, 0, 4,18,12, 0,11, 0, 1,15, 1,15, 4, 2, 0],
            [11,13,12,16, 9,18, 6, 8,18, 1, 5,12,17,13, 5],
            [ 7,17, 2, 5, 0,17, 9,18, 4,13, 6,13, 7, 2, 1],
            [ 2, 3, 9, 0,19, 6, 6,15,14, 4, 8, 1,19, 5, 9],
            [ 3,10, 5,11, 7,14, 1, 5, 3,19,12, 5, 2,13,16],
            [ 0, 8,10,18,17, 5, 5, 8, 2,11, 5,16, 4, 9,14],
            [15, 9,16,18, 9, 5, 2, 5,13, 3,10,19, 9,14, 3],
            [12,11,16, 1,10,12, 6,18, 6, 6,18,10, 9, 5, 2],
            [17, 9, 6, 6,14, 9, 2, 2,13,13,15,17,15, 3,14],
            [18,14,12, 6,18,16, 4,10,19, 5, 6, 8, 9, 1, 6]]

print(pacificAtlantic(heights1))