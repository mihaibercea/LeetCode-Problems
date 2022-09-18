# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
from typing import final


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):

    head = ListNode()    
    to_return = head

    while list1 or list2:       
    
        if list1 and not list2:        
           head.next = ListNode(list1.val)
           list1 = list1.next
           head = head.next
        elif list2 and not list1:
            head.next = ListNode(list2.val)
            list2 = list2.next
            head = head.next
        elif list1 and list2:
            if list1.val<=list2.val:
                head.next = ListNode(list1.val)
                list1 = list1.next
                head = head.next

            elif list2.val<list1.val:
                head.next = ListNode(list2.val)
                list2 = list2.next
                head = head.next

    return to_return.next

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)
head1.next.next.next = ListNode(6)
head1.next.next.next.next = ListNode(7)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(5)


res = mergeTwoLists(head1, head2)

while res:
    print(res.val)
    res = res.next

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)