# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

 

# Example 1:



# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# Example 2:



# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# Example 3:

# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.
 

# Constraints:

# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right      

def traverse(root, ref, count):

    if not root:
        return count
    
    if root.val>=ref:
        count+=1
        count = traverse(root.left, root.val, count)
        count = traverse(root.right, root.val, count)
    
    elif root.val<ref:
        count = traverse(root.left, ref, count)
        count = traverse(root.right, ref, count)    
    return count

def goodNodes(root: 'TreeNode') -> int:

    count = 0
    
    ref = root.val
        
    count = traverse(root, ref, count)

    return count

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

print(goodNodes(root1))

#LeetCode Solution

