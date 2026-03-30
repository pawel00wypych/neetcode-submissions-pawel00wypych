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
        while cur and cur.val != key:
            parent = cur
            if cur.val > key:
                cur = cur.left
            elif cur.val < key:
                cur = cur.right

        if not cur:
            return root

        if not cur.left:
            if not parent:
                return root.right
            else:
                if cur.val > parent.val:
                    parent.right = cur.right
                else:
                    parent.left = cur.right
            del cur
            return root
        elif not cur.right:
            if not parent:
                return root.left
            else:
                if cur.val > parent.val:
                    parent.right = cur.left
                else:
                    parent.left = cur.left
            del cur
            return root
        else:
            min_right_node = cur.right
            min_right_node_parent = cur
            while min_right_node.left:
                min_right_node_parent = min_right_node
                min_right_node = min_right_node.left
            
            if min_right_node_parent == cur:
                cur.val  = min_right_node.val
                cur.right = min_right_node.right
                del min_right_node
                return root
            else:
                min_right_node_parent.left = min_right_node.right
                min_right_node.right = cur.right
                min_right_node.left = cur.left

                if not parent:
                    del cur
                    return min_right_node
                else:
                    if cur.val < parent.val:
                        parent.left = min_right_node
                    else:
                        parent.right = min_right_node
                del cur
                return root

