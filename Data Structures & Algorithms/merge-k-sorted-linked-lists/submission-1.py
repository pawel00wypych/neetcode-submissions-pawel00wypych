# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        if len(lists) <= 1:
            return lists[0]

        m = int(len(lists)/2)
        L = self.mergeKLists(lists[:m])
        R = self.mergeKLists(lists[m:])

        merged = self.merge_list_nodes(L, R)
        return merged

    def merge_list_nodes(self, l_h, r_h):
        merged = None
        if not l_h: return r_h
        if not r_h: return l_h

        if l_h.val <= r_h.val:
            merged = l_h
            if l_h.next:
                l_h = l_h.next
            else:
                merged.next = r_h
                return merged
        else:
            merged = r_h
            if r_h.next:
                r_h = r_h.next
            else:
                merged.next = l_h
                return merged

        merged_pointer = merged
        while l_h and r_h:
            if l_h.val <= r_h.val:
                merged_pointer.next = l_h
                l_h = l_h.next
                merged_pointer = merged_pointer.next
            else:
                merged_pointer.next = r_h
                r_h = r_h.next
                merged_pointer = merged_pointer.next

        if r_h:
            merged_pointer.next = r_h
        elif l_h:
            merged_pointer.next = l_h

        return merged
