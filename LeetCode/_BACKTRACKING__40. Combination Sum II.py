# 40. Combination Sum II
# Medium

# 6819

# 167

# Add to List

# Share
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

def combinationSum2(candidates, target):        

    def backtrack(candidates, curr = [], sum=0):

        if sum == target:
            curr = sorted(curr)
            if curr not in res:
                res.append(curr[:])
                return        
        
        for i in range(len(candidates)):
            curr.append(candidates[i])
            sum+=candidates[i]
            backtrack(candidates[:i]+candidates[i+1:], curr, sum)
            sum-=candidates[i]
            curr.pop()    

    res = []
    candidates = sorted(candidates)    
    for i in range(len(candidates)):
        if candidates[i]>target:
            candidates = candidates[:i]
            break
    
    testSum=0
    for i in range(len(candidates)):
        testSum+=candidates[i]
        
    if testSum>=target:        
        backtrack(candidates)    
        return res
    else:
        return []

candidates = [4,1,1,4,4,4,4,2,3,5]
target = 10
print(combinationSum2(candidates, target))