# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

# Accepted
# 922,718
# Submissions
# 1,338,125

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right      

def traverse(root, k, array):

    if not root:
        return array
    
    elif root.left:
        array = traverse(root.left, k, array)
    
    if len(array)<k:
        array.append(root.val)
        
        if root.right:
            array = traverse(root.right, k, array)

    return array   
   

def kthSmallest(root: 'TreeNode', k: 'int') -> int:
    
    array = []

    array = traverse(root, k, array)

    return array[-1]

       

root1 = TreeNode(1)
root1.right = TreeNode(2)
# root1.left = TreeNode(1)
# root1.left.right = TreeNode(2)

# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(kthSmallest(root1, 2))

#LeetCode Solution

