# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev_p = None
        next_p = head

        
        while cur:
            next_p = cur.next
            cur.next = prev_p
            prev_p = cur
                
            if not next_p:
                head = cur
                return head
            
            cur = next_p

        return head