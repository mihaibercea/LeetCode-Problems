# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2



#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def calcDepth(root, currentDepth, maxD):
    if not root.left and not root.right:
        currentDepth+=1
        if currentDepth>maxD:
            maxD = currentDepth
        return maxD
    else:
        currentDepth+=1
        if root.right and not root.left:            
            maxD = calcDepth(root.right, currentDepth, maxD)
        elif root.left and not root.right:            
            maxD = calcDepth(root.left, currentDepth, maxD)
        else:        
            splitDepth=currentDepth
            maxD = calcDepth(root.left, currentDepth, maxD)
            currentDepth = splitDepth
            maxD = calcDepth(root.right, currentDepth, maxD)
    
    return maxD

def maxDepth(root):       

    maxD = 0
    currentDepth = 0 
    
    if root == None:
            return maxD

    maxD = calcDepth(root, currentDepth, maxD)

    return maxD


root1 = TreeNode(3)
root1.right = TreeNode(20)
root1.left = TreeNode(9)
root1.right.right = TreeNode(7)
root1.right.left = TreeNode(15)

print(maxDepth(root1))
