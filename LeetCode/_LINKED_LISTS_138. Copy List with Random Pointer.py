# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

 

# Example 1:


# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]


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
    temp = Node
    temp.val = x
    temp.next = node.next.next
    node.next = temp

def reverseList(head):

    reversed = Node(head.val)   

    while head.next:
        temp = Node(head.next.val)
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


def copyRandomList(head):

    if head == None:
            return None
    
    #Creates a list of the object, value and 0. 0 Stands for the future index of the random node it points to, from the same list.

    listNodes = []
    listRandoms = []

    toModify = head
    
    while toModify:
        listNodes.append(toModify)
        toModify = toModify.next 

    #Add the indices as well
    toModify = head

    while toModify:
        if toModify.random:
            listRandoms.append(listNodes.index(toModify.random))
        else:
            listRandoms.append(None)

        toModify = toModify.next

    # # for item in theList:
    # #     for otherItem in theList:
    # #         if item[0].random == otherItem[0]:
    # #             item[2] = theList.index(otherItem)
    # #         else:
    # #             item[2] = None
        
    #Initiate the new head as an empty node

    newHead = Node(0)

    toModify = newHead

    #Create the linked list, without the random pointers. Use the listNodes for the values.

    for item in listNodes:
        toModify.val = item.val
        
        if listNodes.index(item) == len(listNodes) -1:
            toModify.next = None

        else:
            toModify.next = Node(0)
            toModify = toModify.next

    toModify = newHead

    #Create a new list with all the Nodes of the new linked list.

    newListNodes = []

    while toModify:
        newListNodes.append(toModify)
        toModify = toModify.next 

    toModify = newHead

    #Create the random indices based on the indices from listRandoms.

    for index in listRandoms:
        if index!=None:
            toModify.random = newListNodes[index]
        else:
            toModify.random = index
        
        toModify = toModify.next

    return newHead

        
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(4)
head1.next.next.next = Node(6)
head1.next.next.next.next = Node(7)
head1.random = None
head1.next.random =head1.next.next.next
head1.next.next.random = head1
head1.next.next.next.random = head1.next
head1.next.next.next.next.random = head1

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(5)

res = copyRandomList(head1)

while res:
    print(res.val)
    if res.random:
        print(res.random.val)
    else:
        print('None')
    res = res.next

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)