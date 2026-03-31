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

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right or not root.left: # 1 or 0 children
                return root.right if root.right else root.left
            else:   # 2 children
                cur = root.right
                while cur.left: # find the smallest node from right subtree
                    cur = cur.left

                root.val = cur.val
                root.right = self.deleteNode(root.right, root.val)

        return root

            

            