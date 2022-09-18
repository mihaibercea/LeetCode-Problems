from itertools import count
from textwrap import fill
from turtle import left, right
import numpy as np

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.data = key

# def fillTree(root):
#     root.key = n
#     if n-1 == 0:
#         return root
#     elif n-2 == 0:
#         root.left = Node(n-1)
#         return root
#     else:
#         newRoot = root
#         root.left = Node(n-1)
#         root.right = Node(n-2)

def solution(n):
    stepOne = 1
    stepTwo = 1
    total = 0

    if n<=1:
        total = 1
    else:
        for step in range(n-1):
            total = stepOne + stepTwo
            stepTwo = stepOne
            stepOne = total            
    return total
          

print("what is your numner?\n")
n = input()
n = int(n)

print(solution(n))


# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
        