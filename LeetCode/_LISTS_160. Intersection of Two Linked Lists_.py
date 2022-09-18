# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge(head, headB):
    
    while True:
        if head.next == None:
            head.next = headB
            break
        else:
            head = head.next

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        node = slow
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return node
    return None

def getIntersectionNode(headA, headB):
    slow = headA
    fast = headB
    #slower = None
    #fastish = None
    
    while slow:
        # if (slower!=None and fastish !=None) and slower==fastish:
        #     return slower
        if slow == fast:
            return slow
            break
        #slower = slow
        if slow.next == None:  
            slow = headA
        else:
            slow = slow.next

        if fast.next==None:
            # fastish = headB            
            fast=headB.next                       
        elif fast.next.next==None:
            # fastish = fast.next               
            fast=headB                        
        else:    
            # fastish = fast.next 
            fast = fast.next.next
            
        
    return None        
    
headC = ListNode(6)
headC.next = ListNode(7)

headA = ListNode(1)
headA.next = headC

headB = ListNode(4)
headB.next = headC

print(getIntersectionNode(headA, headB))