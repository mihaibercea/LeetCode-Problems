# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

from sys import last_traceback
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


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.visited = ListNode('Head')
        self.last_visited = self.visited
        
    def get(self, key: int) -> int:
        if key in self.d.keys():
            return self.d[key]

    def put(self, key: int, value: int) -> None:
        self.len = len(self.d)
        if self.len<self.capacity:
            self.d[key] = value
            self.last_visited.next = ListNode(key)
            self.last_visited = self.last_visited.next           
        elif self.len == self.capacity:
            del self.d[self.last_visited.val]
            self.d[key] = value
            self.last_visited = self.visited
            while self.last_visited.next.next:
                self.last_visited = self.last_visited.next
            self.last_visited.next = ListNode(key)
            self.last_visited = self.last_visited.next  



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

        
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