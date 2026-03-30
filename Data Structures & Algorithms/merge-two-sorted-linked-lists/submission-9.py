# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        cur1 = list1
        cur2 = list2

        # wybór head
        if cur1.val <= cur2.val:
            head = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur2 = cur2.next

        prev = head   # to jest minimalny brakujący klocek

        # merge
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                prev.next = cur1
                cur1 = cur1.next
            else:
                prev.next = cur2
                cur2 = cur2.next
            prev = prev.next

        # dopięcie ogona
        prev.next = cur1 if cur1 else cur2
        return head