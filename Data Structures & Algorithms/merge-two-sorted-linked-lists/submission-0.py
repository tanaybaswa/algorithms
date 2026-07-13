# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode()


        l = list1
        r = list2
        curr = sentinel

        while l and r:

            if l.val < r.val:
                curr.next = l

                l = l.next
                curr = curr.next

            else:
                curr.next = r

                r = r.next
                curr = curr.next

        while l:
            curr.next = l

            l = l.next
            curr = curr.next

        while r:
            curr.next = r

            r = r.next
            curr = curr.next

        
        return sentinel.next
        