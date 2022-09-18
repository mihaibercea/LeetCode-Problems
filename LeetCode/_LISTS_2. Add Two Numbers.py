# Definition for singly-linked list.
from re import L
from traceback import print_tb


class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

      

def addTwoNumbers_normalOrder(self, l1, l2):

    l1_copy = ListNode()
    l1_copy.next = l1.next
    l1.copy.val = l1.val
    l2_copy = ListNode()
    l2_copy.next = l2.next
    l2.copy.val = l2.val

    sum = ListNode()

    a = pop_end(l1)
    b = pop_end(l2)
    extra = ListNode(0)



def insert_node(l, node):
    temp = ListNode()
    temp.val = l.val
    temp.next = l.next
    l.val = node.val
    l.next = temp



def pop_end(l):
    while l.next.next:
        l = l.next
    node = l.next 
    l.next = None
    return node
    
   
def to_end(l, l_copy):
    if l.next == None:        
        return l    
    else:
        l = l.next
        return to_end(l)


def addTwoNumbers(l1, l2):

    sum = ListNode(0)
    sum_head = sum
    extra = 0

    while l1 and l2:

        sum.val = (l1.val + l2.val + extra)%10
        extra = (l1.val + l2.val + extra)//10
        l1 = l1.next
        l2 = l2.next
        sum.next = ListNode(0)
        sum = sum.next

    if l1 == None == l2:
        if extra !=0:
            sum.val = extra
        else:
            sum = sum_head
            while sum.next:
                if sum.next.val == 0 and sum.next.next == None:
                    sum.next = None
                    break
                sum = sum.next
        
    elif l1==None:
        sum.val = (l2.val + extra)%10
        extra = (l2.val + extra)//10
        if extra > 0:
            sum.next = ListNode(extra)
        
        
    elif l2==None:
        sum.val = (l1.val + extra)%10
        extra = (l1.val + extra)//10
        if extra > 0:
            sum.next = ListNode(extra)
        elif sum.val == 0 == extra:
            sum = None

    return sum_head   

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result1 = addTwoNumbers(l1, l2)

def print_list(l):
    while l!=None:
        print(l.val)
        l = l.next

print_list(result1)
