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

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right and not root.left:
                root = None
            elif root.right and not root.left:
                root.val = root.right.val
                self.deleteNode(root.right, root.val)
                return root.right
            elif root.left and not root.right:
                root.val = root.left.val
                self.deleteNode(root.left, root.val)
                return root.left
            else:
                min_node = self.findMin(root.right)
                root.val = min_node
                root.right = self.deleteNode(root.right, root.val)

        return root

    def findMin(self, root: Optional[TreeNode]):
        while root and root.left:
            root = root.left
        return root.val