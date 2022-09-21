# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    # Write your code here.
    l = []
    to_manipulate = head
    
    if head ==None:
        return None

    else:    
        while to_manipulate!=None:
            l.append(to_manipulate)
            to_manipulate = to_manipulate.next

        if k!=0:
            k = k%len(l)
    
        tail = l[-k]        
        l[-k-1].next=None

        head = tail
    
        while tail.next!=None:
            tail = tail.next
    
        tail.next = l[0]

        while head!=None:
            print(head.value)
            head = head.next

head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(5)

shiftLinkedList(head, -18)