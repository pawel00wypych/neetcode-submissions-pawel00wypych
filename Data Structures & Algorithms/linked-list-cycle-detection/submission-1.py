# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        i = 0


        while cur:
            if i > 1000:
                return True
            cur = cur.next
            i += 1

        return False