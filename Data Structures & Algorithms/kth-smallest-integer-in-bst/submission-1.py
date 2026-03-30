# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        inorder_nodes = []
        cur = root
        stack.append(cur)
        while cur or stack or len(inorder_nodes) < k:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            inorder_nodes.append(cur.val)
            cur = cur.right

        return inorder_nodes[k-1]
            

