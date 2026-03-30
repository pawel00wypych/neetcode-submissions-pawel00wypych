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
            if cur.val < key:
                cur = cur.right
            else:
                cur = cur.left

        if not cur:
            return root

        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not parent:
                root = child
            else:
                if cur.val < parent.val:
                    parent.left = child
                else:
                    parent.right = child
        else:
            child = cur.right
            par = cur
            while child.left:
                par = child
                child = child.left

            if par != cur:
                par.left = child.right
                child.right = cur.right

            child.left = cur.left
            
            if not parent:
                root = child
            else:
                if cur.val < parent.val:
                    parent.left = child
                else:
                    parent.right = child

        return root