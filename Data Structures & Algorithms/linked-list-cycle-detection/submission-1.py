# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        """
        we can use a fast and slow pointer to solve this? that should work for odd and even cycles right? 


        """
        if not head: 
            return False

        slow = head
        fast = head.next

        while slow and fast and fast.next:

            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
        