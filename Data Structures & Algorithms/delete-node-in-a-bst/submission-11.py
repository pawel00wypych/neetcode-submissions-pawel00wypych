# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        cur = root
        parent = None
        cur_is_right_child = True
        while cur and cur.val != key:
            parent = cur
            if cur.val > key:
                cur_is_right_child = False
                cur = cur.left
            elif cur.val < key:
                cur_is_right_child = True
                cur = cur.right

        if not cur:
            return root

        if not cur.left:
            if not parent:
                return cur.right

            new_child = cur.right
            if cur_is_right_child:
                parent.right = new_child
            else:
                parent.left = new_child
            del cur
            return root
        elif not cur.right:
            if not parent:
                return cur.left

            new_child = cur.left
            if cur_is_right_child:
                parent.right = new_child
            else:
                parent.left = new_child
            del cur
            return root
        else:
            
            min_right = cur.right
            min_right_parent = cur
            while min_right.left:
                min_right_parent = min_right
                min_right = min_right.left

            if not parent:
                if min_right_parent == cur:
                    min_right.left = cur.left
                    del cur
                    return min_right
                else:
                    min_right_parent.left = min_right.right
                    min_right.left = cur.left
                    min_right.right = cur.right
                    del cur
                    return min_right
            else:
                if min_right_parent == cur:
                    if cur_is_right_child:
                        parent.right = min_right
                    else:
                        parent.left = min_right
                    min_right.left = cur.left
                    del cur
                    return root
                else:
                    min_right_parent.left = min_right.right
                    min_right.left = cur.left
                    min_right.right = cur.right
                    if cur_is_right_child:
                        parent.right = min_right
                    else:
                        parent.left = min_right
                    del cur
                    return root