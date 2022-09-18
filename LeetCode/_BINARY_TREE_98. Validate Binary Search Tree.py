# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right      

def traverse(root, ref_to_left, ref_to_right):

    if not root:
        return True       
    
    if ref_to_left:
        for r in ref_to_left:
            if root.val<=r:
                return False
    if ref_to_right:
        for r in ref_to_right:
            if root.val>=r:
                return False
    
    return traverse(root.right, ref_to_left + [root.val], ref_to_right) and traverse(root.left, ref_to_left, ref_to_right + [root.val])


def isValidBST(root: 'TreeNode') -> bool:
    
    ref_to_left = []
    ref_to_right = []
    return traverse(root, ref_to_left, ref_to_right)
       

root1 = TreeNode(32)
root1.right = TreeNode(47)
root1.left = TreeNode(26)
root1.right.right = TreeNode(56)

root1.left.left = TreeNode(19)
root1.left.left.right = TreeNode(27)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(isValidBST(root1))

#LeetCode Solution

