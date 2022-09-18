# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
    

from itertools import count


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next             
        
def countList(list):
    count = 1
    while list.next:
        count+=1
        list = list.next
    return count


def removeNthFromEnd(head, n):
    if n == 0:
        return head      
    else:
        to_return = head
        len = countList(head)
        if len == n:
            return head.next
        pos = len - n
        pointer = 1

        while pointer<pos:
            head = head.next
            pointer+=1
        head.next = head.next.next
        
        return to_return

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

res = removeNthFromEnd(head1, 2)

while res:
    print(res.val)
    res = res.next

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)