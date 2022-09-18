# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

import string


class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if self.minstack:
            self.minstack.append(min(self.minstack[-1], val))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.minstack[-1]


def evalRPN(tokens):
    exp = []
    calc = 0
    for item in tokens:
        if item.strip('-').isnumeric():
            if item[0] != '-':
                exp.append(int(item))
            else:
                exp.append(0-int(item.strip('-')))
        else:
            if item == '+':                
                calc = exp[-2]+exp[-1]
                exp.pop()
                exp.pop()
                exp.append(calc)
            elif item == '-':
                calc = exp[-2]-exp[-1]
                exp.pop()
                exp.pop()
                exp.append(calc)
            elif item == '*':
                calc = exp[-2]*exp[-1]
                exp.pop()
                exp.pop()
                exp.append(calc)
            elif item == '/':
                calc = int(exp[-2]/exp[-1])
                exp.pop()
                exp.pop()
                exp.append(calc)

    return exp[-1]                

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))
