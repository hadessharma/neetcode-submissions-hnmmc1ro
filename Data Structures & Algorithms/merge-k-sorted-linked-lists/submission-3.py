# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        res = ListNode()
        prev = res
        temp = 1

        for l in lists:
            if not l:
                continue
            heapq.heappush(min_heap, [l.val, temp, l])
            temp += 1
        
        while min_heap:
            top = heapq.heappop(min_heap)
            prev.next = top[2]
            prev = prev.next
            nxt = top[2].next
            if nxt:
                heapq.heappush(min_heap, [nxt.val, temp, nxt])
                temp += 1
                
        
        return res.next
