# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        [0, 1, 2, 3, 4, 5, 6]
        0 1 2 3 | 4 5 6
        6 5 4
        0 6 1 
        '''
        if not head:
            return None

        slow, fast = head, head.next

        while fast and fast.next and slow:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        first = head
        # print(slow.val)
        # reverse second
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev

        while second and first:
            second_nxt = second.next
            first_nxt = first.next
            
            first.next = second
            second.next = first_nxt

            first = first_nxt
            second = second_nxt
        
        # return head
