# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right      

def traverse(root, d, level):

    if not root:
        return d

    else:
        if level in d.keys():
            d[level].append(root.val)
        else:
            d[level] = [root.val]

        d = traverse(root.right, d, level+1)
        d = traverse(root.left, d, level+1)

    return d

def rightSideView(root: 'TreeNode') -> int:
    
    d = {}
    level = 0
    res = [] 
    d = traverse(root, d, level)
    
    for key in d.keys():
        res.append(d[key][0])
    return res


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

print(rightSideView(root1))

#LeetCode Solution

