# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        [1,2,3,4]
           ^
        """
        dummy = ListNode(0, head)
        fast = head
        slow = dummy

        while n and fast:
            fast = fast.next
            n -= 1
        
        while fast and slow:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next
