from collections import defaultdict


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

node = Node(1)

nodeCopy = Node(node.val)

d = defaultdict()
d[node] = nodeCopy

print(d)
if d[1]:
    print