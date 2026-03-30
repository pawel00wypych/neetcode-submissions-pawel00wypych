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
        inorder_nodes.extend(self.inorderTraversal(root.left))
        inorder_nodes.append(root.val)
        inorder_nodes.extend(self.inorderTraversal(root.right))
        return inorder_nodes