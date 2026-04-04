# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        cur = root
        balanced = True
        stack = []

        def postorder(root: Optional[TreeNode]) -> int:
            nonlocal balanced
            if not root:
                return 0

            left = postorder(root.left)
            right = postorder(root.right)
            if abs(left - right) > 1:
                balanced = False
            return 1 + max(left, right)

        postorder(root)
        return balanced 