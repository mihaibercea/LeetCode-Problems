# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false

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
    
def isSameTree(p, q) -> bool:

    if not p and not q:
        return True

    elif (not p and q) or (not q and p):
        return False

    else:
        if p.val !=q.val:
            return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    
    
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

