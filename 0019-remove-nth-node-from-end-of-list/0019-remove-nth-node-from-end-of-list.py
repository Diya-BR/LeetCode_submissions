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
        print(f"{n_count}")
        temp = head
        if n_count == n:
            return head.next
        print(f"{temp}")

        while i < (n_count - n - 1):
            temp = temp.next
            i += 1
        temp.next = temp.next.next
        return head
