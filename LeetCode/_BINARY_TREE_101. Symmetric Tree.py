# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# left nodes = mirrored right nodes

from operator import truediv
from sre_constants import SRE_FLAG_IGNORECASE


class Solution(object):

    def inorderTraverse(self, root):
        result = []
        self.traverse(root, result)
        return result
    
    def mirrorOrderTraverse(self, root):
        result = []
        self.mirrorTraverse(root, result)
        return result

    def traverse(self, root, result):
        
        if root == None:
            return
        else:
            self.traverse(root.left, result)
            result.append(root.val)
            self.traverse(root.right, result)
    
    def mirrorTraverse(self, root, result):
    
        if root == None:
            return
        else:
            self.traverse(root.right, result)
            result.append(root.val)
            self.traverse(root.left, result)
    
    def isSymmetric(self, root):
        result1 = self.mirrorOrderTraverse(root.left)
        result2 = self.inorderTraverse(root.right)

        if result1==result2:
            return True
        else:
            return False
    