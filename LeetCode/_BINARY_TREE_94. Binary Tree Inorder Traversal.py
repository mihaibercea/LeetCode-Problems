# Definition for a binary tree node.
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val):
        self.key = val
        self.right = None
        self.left = None


class Solution(object):
    def traverse(self, root, result):
        
        if root==None:
            return
        else:
            self.traverse(root.left, result)
            result.append(root.val)
            self.traverse(root.right, result)
            
    def inorderTraversal(self, root):
        result=[]
        self.traverse(root, result)
        return result