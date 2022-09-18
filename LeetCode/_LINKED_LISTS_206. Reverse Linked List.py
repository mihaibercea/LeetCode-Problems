# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
    

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next             
        
def reverseList(head):
    if (head == None or head.next == None):
            return head
    last = reverseList(head.next)
    head.next.next = head
    head.next = None
    return last


def reverseListIterative(list):

    reversed = ListNode(list.val)   

    while list.next:
        temp = ListNode(list.next.val)
        temp.next = reversed
        reversed = temp       
        list = list.next

    return reversed

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

res = reverseListIterative(head1)

while res:
    print(res.val)
    res = res.next

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)