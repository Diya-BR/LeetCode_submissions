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
        map_all = {}
        def helper(node: 'Optional[Node]') -> 'Optional[Node]':
            if not node:
                return None
            if node not in map_all:
                map_all[node] = Node(node.val)
                map_all[node].next = helper(node.next)
                map_all[node].random = helper(node.random)
            return map_all[node]
        map_all[head] = helper(head)
        return map_all[head]


        '''temp = head
        while temp:
            map_all[temp] = Node(temp.val)
            temp = temp.next
        map_all[None] = None
        temp = head
        print(f"{map_all}")
        while temp:
            node = map_all[temp]
            node.next = map_all[temp.next]
            node.random = map_all[temp.random]
            temp = temp.next
        return map_all[head]'''
