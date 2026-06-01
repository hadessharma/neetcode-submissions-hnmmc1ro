# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSub(self, p, q):
        if not p and not q:
            return True
        
        if p and q and q.val == p.val:
            return (
                self.isSub(p.left, q.left) and
                self.isSub(p.right, q.right)
            )
        
        return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if root.val == subRoot.val:
            if (
                self.isSub(root.left, subRoot.left) and 
                self.isSub(root.right, subRoot.right)
            ):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        