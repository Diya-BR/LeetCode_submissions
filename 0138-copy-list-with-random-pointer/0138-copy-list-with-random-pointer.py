"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodemap = {}
        def helper(node: 'Optional[Node]') -> 'Optional[Node]':
            if not node:
                return None
            if node not in nodemap:
                nodemap[node] = Node(node.val)
                nodemap[node].next = helper(node.next) 
                nodemap[node].random = helper(node.random) 
            return nodemap[node]
        # node_head = helper(head)
        return helper(head)
            
