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
    
    listhead = []
    while head.next:
        listhead.append(head.val)
        head = head.next
    listhead.append(head.val)

    newhead = ListNode(listhead[-1])
    temp = newhead

    for i in range(len(listhead) -2, -1, -1):
        temp.next = ListNode(listhead[i])
        temp = temp.next

    return newhead




head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

res = reverseList(head1)

while res:
    print(res.val)
    res = res.next

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)