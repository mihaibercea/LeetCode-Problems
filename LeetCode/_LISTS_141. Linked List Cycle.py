# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def check_list(head, L):

    if head.next == None:
        return False
    
    elif head.next in L:
        return True

    else:
        L.append(head)        
        return check_list(head.next, L)
           

def hasCycle(head):
    L = []
    return check_list(head, L)

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(1)
head1.next.next.next = head1

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(1)

print(hasCycle(head1))
print(hasCycle(head2))


def hasCycle_leetcodePro(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False