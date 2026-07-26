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
        temp = head
        dict_head = {}
        while temp:
            dict_head[temp] = ListNode(temp.val)
            temp= temp.next
        dict_head[None] = None
        temp = head
        temp_head = dict_head[temp]
        temp_new =  temp_head
        while temp:
            temp_new.next =  dict_head[temp.next]
            temp_new.random = dict_head[temp.random]
            temp = temp.next
            temp_new = temp_new.next
        return temp_head

