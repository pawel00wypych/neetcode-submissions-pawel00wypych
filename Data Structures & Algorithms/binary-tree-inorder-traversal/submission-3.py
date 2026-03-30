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
        stack.append(cur)
        while stack != []:
            while cur.left and cur.left.val not in inorder_nodes:
                cur = cur.left
                stack.append(cur)

            cur = stack.pop()
            inorder_nodes.append(cur.val)
            if cur.right and cur.right.val not in inorder_nodes:
                cur = cur.right
                stack.append(cur)

        return inorder_nodes


        