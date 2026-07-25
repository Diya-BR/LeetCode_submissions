# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        hold_all = []
        while head:
            hold_all.append(head)
            head = head.next
        l, r = 0, len(hold_all)-1
        while l < r:
            hold_all[l].next = hold_all[r]
            l += 1
            if l == r: break
            hold_all[r].next = hold_all[l]
            r -= 1
        hold_all[l].next = None
        
        
        