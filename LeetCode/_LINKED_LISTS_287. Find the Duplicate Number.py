# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?


from typing import List


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
    temp = ListNode(x)
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


def findDuplicate(nums):

    d = {}

    for num in nums:
        if num in d.keys():
            d[num]+=1
        else:
            d[num]=0

        if d[num]>0:
            return num

def findDuplicateWithLists(nums):

    head = ListNode(nums[0])

    toModify = head

    for item in nums[1:]:
        if item < head.val:
            temp = ListNode(item)
            temp.next = head
            head = temp
        else:
            while toModify:
                if item == toModify.val:
                    return item
                elif toModify.next:
                    if item < toModify.next.val:
                        temp = ListNode(item)
                        temp.next = toModify.next
                        toModify.next = temp
                        break
                if not toModify.next:
                    tail = ListNode(item)
                    toModify.next=tail
                    break
                toModify = toModify.next
                             
        toModify = head
        


        
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(4)
head1.next.next.next = Node(6)
head1.next.next.next.next = Node(7)


head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = head2

nums1 = [1,3,4,2,2]

print(findDuplicateWithLists(nums1))

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