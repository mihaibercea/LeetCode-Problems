# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right      
    
def isInBranch(root, p):

    if root == None:
        return False
    
    if root.val == p.val:
        return True   
          
    else:
        return isInBranch(root.left, p) or isInBranch(root.right, p)

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
    if (isInBranch(root.left, p) and isInBranch(root.left, q)):
        return lowestCommonAncestor(root.left, p, q)
    elif (isInBranch(root.right, p) and isInBranch(root.right, q)):
        return lowestCommonAncestor(root.right, p, q)
    
    else:
        return root.val


root1 = TreeNode(6)
root1.right = TreeNode(8)
root1.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.left.right.left = TreeNode(3)
root1.left.right.right = TreeNode(5)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(9)

p = root1.left.right.left
q = root1.left.right.right

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(lowestCommonAncestor(root1, p, q))

#LeetCode Solution

