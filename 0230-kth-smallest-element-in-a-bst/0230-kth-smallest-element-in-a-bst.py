# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.step = 0
        self.result = None
        def inorder(node: Optional[TreeNode]) -> None:
            if not node or self.result:
                return 
            inorder(node.left)

            if not self.result:
                self.step += 1
                if self.step == k:
                    self.result = node.val 
           
            inorder(node.right)
        inorder(root)
        return self.result
            

        