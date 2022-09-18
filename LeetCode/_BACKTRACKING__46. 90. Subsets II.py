# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

def subsetsWithDup(nums):

    def backtrack(nums, curr = []):
        if len(curr) == k and curr not in res:
            res.append(curr[:])
        
        for i in range(len(nums)):
            curr.append(nums[i])            
            backtrack(nums[i+1:], curr)
            curr.pop()    

    res = []
    n = len(nums)+1
    nums = sorted(nums)
    for k in range(n):
        backtrack(nums)    
    return res

nums = [1, 2, 2]
target = 7
print(subsetsWithDup(nums))
