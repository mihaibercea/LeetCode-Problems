# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

class Node:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.left = None

def creatingP(open, closed, head, res, current):
    if open == 0 and closed == 0:
        head.val=current
        res.append(head.val)
        return head
    elif open == 0 and closed >0:
        head.right = creatingP(open, closed-1, head, res, current+')')
    elif open>0:
        if open == closed:            
           head.left = creatingP(open-1, closed, head, res, current+'(')
        else:
            head.left = creatingP(open-1, closed, head, res, current+'(')
            head.right = creatingP(open, closed-1, head, res, current+')')
            
def generateParenthesis(n):

    open = n
    closed = n
    res = []
    current = ''
    head = Node('')
    creatingP(open, closed, head, res, current)
    return res

n = 3
print(generateParenthesis(n))



