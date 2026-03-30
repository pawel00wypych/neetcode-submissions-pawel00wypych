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

        cur = root
        parent = None
        while cur and cur.val != key: #We are looking for the key in the tree if it exists
            parent = cur
            if cur.val < key:
                cur = cur.right
            elif cur.val > key:
                cur = cur.left
        
        if not cur: # There was no key in the tree
            return root

        # If the key was found lets check how many children does it have
        if not cur.right or not cur.left:
            # 0 or 1 child found
            child = cur.right if cur.right else cur.left
            if parent:
                if parent.left == cur:
                    parent.left = child
                else:
                    parent.right = child
                return root
            else:
                return child
        else:
            # 2 children found
            delNode = cur
            par = cur
            cur = delNode.right
            while cur.left: # find smallest node from right subtree
                par = cur
                cur = cur.left 

            if cur != delNode.right:
                par.left = cur.right
                cur.right = delNode.right

            cur.left = delNode.left     
                
            if parent:
                if parent.left == delNode:
                    parent.left = cur
                else:
                    parent.right = cur
            else:
                return cur
        return root