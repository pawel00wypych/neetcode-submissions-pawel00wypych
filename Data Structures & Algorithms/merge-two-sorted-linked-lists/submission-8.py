# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        if not cur1:
            return cur2
        if not cur2:
            return cur1

        # ustaw head
        if cur1.val <= cur2.val:
            new_head = cur1
            cur1 = cur1.next
        else:
            new_head = cur2
            cur2 = cur2.next

        tail = new_head

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                tail.next = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                cur2 = cur2.next
            tail = tail.next

        tail.next = cur1 if cur1 else cur2
        return new_head