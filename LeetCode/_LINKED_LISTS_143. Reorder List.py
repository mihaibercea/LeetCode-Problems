# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None


def insert(x, node):
    #insert a node with value 'x' after 'node'
    temp = ListNode
    temp.val = x
    temp.next = node.next.next
    node.next = temp

def reverseList(list):

    reversed = ListNode(list.val)   

    while list.next:
        temp = ListNode(list.next.val)
        temp.next = reversed
        reversed = temp       
        list = list.next        

    return reversed
   
def countList(list):
    count = 1
    while list.next:
        count+=1
        list = list.next
    return count

def reorderList(list):

    if list == None:
        return None
    
    else:            
        reversed = ListNode
        reversed = reverseList(list)        
        count = countList(list)

        if count == 1:
            return list
        else:
            half = count//2
            to_return = list

            while half>0:
                node = ListNode(reversed.val)
                node.next = list.next
                list.next = node
                list = node.next
                if half == 1 and count%2==0:
                    node.next = None                                     
                reversed = reversed.next
                half-=1
            
            if count%2 == 1:
                list.next = None            

        return to_return
        
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)
head1.next.next.next = ListNode(6)
head1.next.next.next.next = ListNode(7)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(5)

res = reorderList(head1)

while res:
    print(res.val)
    res = res.next

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)