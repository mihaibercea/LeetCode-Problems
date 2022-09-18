# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Node:
    def __init__(self, val):
        self.val = val  # Assign data
        self.next = None  # Initialize

def isValid(s):

    head = Node('start')
    
    for c in s:
        if head.next == None:
            head.next = Node(c)
        else:
            check = head

            while check.next.next:
                check = check.next
            
            if ( c == ')' and check.next.val == '(' ):
                check.next = None
            elif ( c == ']' and check.next.val == '[' ):
                check.next = None
            elif ( c == '}' and check.next.val == '{' ):
                check.next = None
            else:
                check.next.next = Node(c)

    if head.next:
        return False
    else:
        return True

s1 = "(())[]{}"

print(isValid(s1))