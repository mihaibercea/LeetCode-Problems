# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# left nodes = mirrored right nodes
# check root
# check left and right. They need to march.
# check left side notes == rigth side nodes.

from operator import truediv
import re
from sre_constants import SRE_FLAG_IGNORECASE

def traverse( root, result):
    
    if root==None:
        return
    else:
        traverse(root.left, result)
        result.append(root.val)
        traverse(root.right, result)
        
def inorderTraversal(root):
    result=[]
    traverse(root, result)
    return result

def swapRight(rightroot):
    if rightroot !=None:
        temp = rightroot.left
        rightroot.left = rightroot.right
        rightroot.right = temp
        temp = None
    swapRight(rightroot.left)
    swapRight(rightroot.right)

def checkMirror(leftroot, rightroot):
     
    if leftroot==rightroot==None:
        return True
    if (leftroot!=None and rightroot==None) or (leftroot==None and rightroot!=None) or (leftroot.val != rightroot.val):
       return False
    return (checkMirror(leftroot.right, rightroot.left) and checkMirror(leftroot.left, rightroot.right))
      

def isSymmetric(root):
    leftroot=root.left
    rightroot=root.right
    return checkMirror(leftroot, rightroot)
      

test1 = TreeNode(1)
test1.left = TreeNode(2)
test1.right = TreeNode(2)
test1.left.left = None
test1.right.right = TreeNode(3)
test1.right.left = None
test1.left.right = TreeNode(4)

print(inorderTraversal(test1))
print(isSymmetric(test1))


   
        
    