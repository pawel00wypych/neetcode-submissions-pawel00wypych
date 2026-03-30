# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = head
        cur_prev = None
        cur_next = cur.next
        while cur:
            cur.next = cur_prev
            cur_prev = cur
            cur = cur_next
            if cur:   
                cur_next = cur.next

        return cur_prev
            