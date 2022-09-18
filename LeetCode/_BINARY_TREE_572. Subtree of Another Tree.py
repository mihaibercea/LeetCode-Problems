# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
 

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right      
    
def isSameTree(p, q):

    if not p and not q:
        return True
    
    elif (not p and q) or (not q and p):
        return False

    else:
        if p.val!=q.val:
            return False
        left = isSameTree(p.left, q.left)
        right = isSameTree(p.right, q.right)
        return left and right

def isSubTree(root, subRoot) -> bool:

    if not subRoot:
        return True

    elif not root and subRoot:
        return False

    elif isSameTree(root, subRoot):
           return True
    else:
        left = isSubTree(root.left, subRoot) 
        right = isSubTree(root.right, subRoot)
        return left or right
    
root1 = TreeNode(3)
root1.right = TreeNode(4)
root1.left = TreeNode(3)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(0)
root1.left.left = TreeNode(1)

root2 = TreeNode(4)
root2.left = TreeNode(1)
root2.right = TreeNode(2)

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(isSubTree(root1, root2))

#LeetCode Solution

