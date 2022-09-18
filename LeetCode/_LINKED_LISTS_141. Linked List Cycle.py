# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.random = None

def insert(x, node):
    #insert a node with value 'x' after 'node'
    temp = ListNode
    temp.val = x
    temp.next = node.next.next
    node.next = temp

def reverseList(head):

    reversed = ListNode(head.val)   

    while head.next:
        temp = ListNode(head.next.val)
        temp.next = reversed
        reversed = temp       
        head = head.next        

    return reversed
   
def countList(head):
    count = 1
    while head.next:
        count+=1
        head = head.next
    return count


def hasCycle(head):

    if head == None:
        return False

    listed = {}

    while head:
        if head in listed.keys():
            return True
        else:
            listed[head] = 0
                       
        head = head.next

    return False

        
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(4)
head1.next.next.next = Node(6)
head1.next.next.next.next = Node(7)


head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = head2

print(hasCycle(head1))

# while res:
#     print(res.val)
#     if res.random:
#         print(res.random.val)
#     else:
#         print('None')
#     res = res.next

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)