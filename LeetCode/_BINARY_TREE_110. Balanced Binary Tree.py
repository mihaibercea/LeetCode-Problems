# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def maxdepth(root) -> int:
    if root == None:
        return 0  
    left_count = maxdepth(root.left)
    right_count = maxdepth(root.right)    
    return  max(left_count, right_count)+1          
    
def isBalanced(root):
    
    if root == None:
        return True
    
    elif root.right==root.left==None:
        return True
    
    else:
        if abs(maxdepth(root.right) - maxdepth(root.left))>1:
            return False
        else:
            return isBalanced(root.left) and isBalanced(root.right)
    
    
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

#LeetCode Solution

