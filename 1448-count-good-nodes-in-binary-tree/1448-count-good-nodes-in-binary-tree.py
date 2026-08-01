# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode,max_val: int) -> int:
            if not node:
                return 0
            good_node = 1 if node.val>=max_val else 0
            max_all = max(node.val, max_val)
            return good_node + dfs(node.left,max_all) + dfs(node.right,max_all)
        return dfs(root,root.val)
