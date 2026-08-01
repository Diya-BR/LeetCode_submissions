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
        def validate(node: Optional[TreeNode],min_val = float('-inf'), max_val = float('inf')):
            if not node:
                return True
            if  node.val >= max_val or node.val<=min_val:
                return False
            
            
            return validate(node.left,min_val,node.val) and validate(node.right,node.val,max_val)

        return validate(root)