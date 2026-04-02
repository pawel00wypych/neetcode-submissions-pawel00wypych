# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def inorder(root: Optional[TreeNode]) -> int:
            nonlocal is_balanced
            if not root:
                return 0

            left_sum = inorder(root.left)
            right_sum = inorder(root.right)

            if abs(left_sum - right_sum) > 1:
                is_balanced = False
            node_sum = 1 + max(left_sum, right_sum)
            return node_sum


        inorder(root)
        return is_balanced