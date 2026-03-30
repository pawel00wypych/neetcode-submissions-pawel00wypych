# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        #if len(lists) <= 1:
         #   return lists[0]

        for i in range(1,len(lists)):
            print(i)
            lists[i] = self.merge_list_nodes(lists[i-1], lists[i])

        return lists[len(lists)-1]

    def merge_list_nodes(self, l_h, r_h):
        merged = ListNode(-1)
        if not l_h: return r_h
        if not r_h: return l_h

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

        return merged.next
