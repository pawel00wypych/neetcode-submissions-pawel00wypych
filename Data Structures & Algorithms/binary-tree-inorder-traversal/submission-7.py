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

        cur = root
        inorder_nodes = []
        stack = []
        stack.append(root)
        while stack:
            while cur.left and cur.left.val not in inorder_nodes:
                # traverse to the left subtree if it wasn't visited
                cur = cur.left
                stack.append(cur)
            cur = stack.pop() # go back to the parent 
            inorder_nodes.append(cur.val) # when we visited whole left subtree we add node.val
            if cur.right: #check if we can visit right subtree
                cur = cur.right
                stack.append(cur)

        return inorder_nodes