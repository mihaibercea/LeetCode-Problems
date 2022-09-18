# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

def searchMatrix(matrix, target):

    i  = 0
    length = len(matrix[0])-1

    if target<matrix[0][0]:
        return False

    while i <= len(matrix) - 1:
        row = matrix[i]
        if target > row[length] and i == len(matrix) - 1:
            return False
        elif target > row[length] and i < len(matrix) - 1:
            i+=1
        else:
            
            l = 0
            r = len(row)-1
            half = l + ((r-l)//2)

            if len(row) == 1 and row[0] == target:
                    return True
            
            else:
                while l<r:
                    if target == row[l]:
                        return True
                    elif target == row[r]:
                        return True
                    elif target > row[half]:
                        l = half+1
                        half = half = l + ((r-l)//2)
                    elif target <= row[half]:
                        r = half
                        half = half = l + ((r-l)//2)

                return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 61
print(searchMatrix(matrix, target))