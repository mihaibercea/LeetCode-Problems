import numpy as np

number = 0

def solution(n, number):

        
    if n==1:
        return 1

    elif n==2:
        return 2

    else:
        number = number + solution(n-1, number) + solution(n-2, number)

    return number
          

print("what is your numner?\n")
n = input()
n = int(n)

print(solution(n, number))


# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
        