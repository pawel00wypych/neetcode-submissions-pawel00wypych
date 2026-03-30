# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        is_balanced = True

        def inorder(root, cur_sum):
            if not root:
                return cur_sum

            left_sum = inorder(root.left, cur_sum)
            right_sum = inorder(root.right, cur_sum)
            if abs(left_sum - right_sum) > 1:
                nonlocal is_balanced
                is_balanced = False
            
            return 1 + max(left_sum, right_sum)

        height = 0
        inorder(root, height)
        return is_balanced