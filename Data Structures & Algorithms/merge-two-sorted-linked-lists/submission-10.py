# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        new_head = ListNode(-1)

        if not list1:
            return list2
        elif not list2:
            return list1

        tail = new_head
        while cur1 and cur2:
            if cur1.val >= cur2.val:
                tail.next = cur2
                tail = tail.next
                cur2 = cur2.next
            else:
                tail.next = cur1
                tail = tail.next
                cur1 = cur1.next
            
        tail.next = cur2 if not cur1 else cur1
        return new_head.next