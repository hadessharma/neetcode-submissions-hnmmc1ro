# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(root, left_val, right_val):
            if not root:
                return True
            
            if left_val < root.val < right_val:
                return (
                    dfs(root.left, left_val, root.val) and
                    dfs(root.right, root.val, right_val)    
                )
            return False

        return dfs(root, float("-inf"), float("inf"))
