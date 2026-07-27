# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        end = head
        dummy_head = ListNode(0)
        dummy = dummy_head
        while start:
            end = start
            i = 1
            while end and i < k:
                end = end.next
                i += 1
            if not end:
                dummy.next = start
                break
            next_start = end.next
            dummy.next = self.reverse_subset(start, end)
            dummy = start
            start = next_start
        return dummy_head.next



    def reverse_subset(self,start: Optional[ListNode], end: Optional[ListNode])-> Optional[ListNode]:
        stop = end.next if end else None
        prev, curr = None, start
        while curr != stop:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return  prev


