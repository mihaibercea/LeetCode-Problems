# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1


#Definition for a binary tree node.

# def calcMaxLeft(root, left, maxLeft):
#     if root.left == None == root.right:
#         if left>maxLeft:
#             maxLeft = left
    
#         return maxLeft

#     else:
#         if root.left:
#             maxLeft = calcMaxLeft(root.left, left+1, maxLeft)

#         if root.right:
#             maxLeft = calcMaxLeft(root.right, left-1, maxLeft)  
    
#     return maxLeft

# def calcMaxRight(root, right, maxRight):
#     if root.left == None == root.right:
#         if right>maxRight:
#             maxRight = right
    
#         return maxRight

#     else:
#         if root.left:
#             maxRight = calcMaxRight(root.left, right-1, maxRight)

#         if root.right:
#             maxRight = calcMaxRight(root.right, right+1, maxRight)  
    
#     return maxRight


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def calcDepth(root, currentDepth, maxD):
    if root ==None:
        return 0
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

def calcDiameter(root, maxDiameter):

    if root == None:
        
        return maxDiameter

    if root.left==root.right == None:
        
        return maxDiameter
    
    else:
        diameter = calcDepth(root.right, 0, 0) + calcDepth(root.left, 0, 0)
        if diameter > maxDiameter:
            maxDiameter = diameter            
        return max((calcDiameter(root.left, maxDiameter), calcDiameter(root.left, maxDiameter)), maxDiameter)

def diameterOfBinaryTree(root):               
    
    maxDiameter = 0   

    if root == None:
        return 0

    return calcDiameter(root, maxDiameter)

    
root1 = TreeNode(1)
root1.right = TreeNode(3)
root1.left = TreeNode(2)
root1.left.right = TreeNode(5)
root1.left.right.left = TreeNode(6)
root1.left.right.left.left = TreeNode(7)
root1.left.right.left.left.left = TreeNode(8)
root1.left.left = TreeNode(4)

root2 = TreeNode(3)
root2.left = TreeNode(2)
root2.right = TreeNode(4)
root2.right.left = TreeNode(1)

print(diameterOfBinaryTree(root1))
