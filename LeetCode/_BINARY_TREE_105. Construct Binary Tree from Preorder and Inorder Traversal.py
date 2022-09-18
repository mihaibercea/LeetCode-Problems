# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

#PREORDER = root, left, right
#INORDER = left, root, right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right      

def traverse(root, preorder, inorder):
    

    if preorder[0]==inorder[0]:
        return root
    
    while preorder:
        if preorder[1] in inorder[:inorder.index(preorder[1])]:
            root.left = traverse(root, preorder[1:], inorder)
        else:
            root.right = traverse(root, preorder[1:], inorder)

    return root
    
def buildTree(preorder: 'list', inorder: 'list') -> 'TreeNode':
    
    root = TreeNode(preorder[0])

    root = traverse(root, preorder, inorder)

    return root




       

root1 = TreeNode(1)
root1.right = TreeNode(2)
# root1.left = TreeNode(1)
# root1.left.right = TreeNode(2)

# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(buildTree(preorder, inorder))

#LeetCode Solution

