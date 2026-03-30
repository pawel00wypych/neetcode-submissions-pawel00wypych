# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        cur = root
        par = None
        while cur:
            par = cur
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                cur = cur.right

        if not par:
            return TreeNode(val)

        if par.val > val:
            par.left = TreeNode(val)
        elif par.val < val:
            par.right = TreeNode(val)
            
        return root

        
