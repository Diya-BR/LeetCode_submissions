# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        dummy_head = ListNode(0) 
        if n==0:
            return dummy_head.next
        while n > 1:
            list1 = lists.pop()
            list2 = lists.pop()
            
            dummy = dummy_head
            n -= 2
            while list1 and list2:
                if list1.val < list2.val:
                    dummy.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    dummy.next = ListNode(list2.val)
                    list2 = list2.next
                dummy = dummy.next
            if list1:
                dummy.next = list1
            else:
                dummy.next = list2
            lists.append(dummy_head.next)
            n += 1
        return lists[-1] 
