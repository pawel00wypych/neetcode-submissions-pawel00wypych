# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        inorder_nodes = []
        stack = []
        cur = root
        while cur or stack:
            while cur: # traverse to the left most node
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            inorder_nodes.append(cur.val) # add visited node every time we go back in the tree
            cur = cur.right

        return inorder_nodes
