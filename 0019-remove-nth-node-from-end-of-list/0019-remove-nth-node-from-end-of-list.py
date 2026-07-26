# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        i = 0
        n_count = 0
        while temp:
            temp = temp.next
            n_count += 1
        temp = head
        if n==n_count:
            return head.next
        while i<(n_count-n-1):
            print(f"{temp.val}\n")
            temp = temp.next
            i += 1
        
        temp.next = temp.next.next
        return head
        